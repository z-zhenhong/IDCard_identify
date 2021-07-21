import cut_text_area as Atc
import siftAlign as Ats
import cv2
from aip import AipOcr
import time

""" 你的 APPID AK SK """
APP_ID = '24511458'
API_KEY = 'NrVbW2kGmNQsI47004QHyUwF'
SECRET_KEY = 'k3iGLx1twoDjRRPteAn6UnXqxATztQ6B'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def get_pic_info(filename):
    image = get_file_content(filename)
    """ 如果有可选参数 """
    options = {}
    options["language_type"] = "CHN_ENG"
    options["detect_direction"] = "false"
    options["detect_language"] = "false"
    options["probability"] = "false"

    """ 带参数调用通用文字识别, 图片参数为本地图片 """
    return client.basicAccurate(image, options)


def formated(res):
    if '姓名' in res:
        res = '姓名: ' + res[2:]
    elif '性别' in res:
        res = '性别: ' + res[2:]
    elif '民族' in res:
        res = '民族: ' + res[2:]
    elif '出生' in res:
        res = '出生: ' + res[2:]
    elif '住址' in res :
        res = '住址: ' + res[2:]
    elif '公民身份号码' in res:
        res = '公民身份号码: ' + res[6:]
    return  res

# 按排列顺序
idb_info_list = ['name', 'sexual', 'nation', 'date', 'addr', 'id']


def pre_processer(path):
    # 0. 摆正身份证背面
    img = cv2.imread(path)
    # img0是摆正好的图片
    
    standimg =  Ats.get_sandard_card(img)


    #获取文字区域
    res_dict = Atc.get_text_area(standimg)

    tmplist = idb_info_list

    # 按顺序保存
    for i in range(len(tmplist)):
        name = tmplist[i]
        img = res_dict[name]
        cv2.imwrite('output'+'\\'+str(i)+'.jpg',img)




if __name__ == '__main__':


    pre_processer('demo.jpg')
    for i in range(6):
        info = get_pic_info('./output/'+str(i)+'.jpg')
        time.sleep(0.5) #识别太快 百度的api会报错
        infolist= info["words_result"]
        res = ''
        for item in infolist:
            res += item['words']
        print(formated(res))

