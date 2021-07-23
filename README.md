# 身份证识别

## 0.  项目简介

**a提取一张正常拍摄的身份证图片的信息。**

**b支持识别各种正常角度的身份证图片。**

 

**效果预览**

![img](https://gitee.com/chzarles/images/raw/master/imgs/clip_image002.jpg)

​                图1 效果

**下面是简单的步骤分析**

## 1.  图像校正

图像校正的意思是将原图片里旋转的或者歪扭的身份证变换成水平方正的样子。主要用到SIFT特征点匹配来匹配图中身份证的位置，并调用透视变换来把身份证摆正。摆正后的图片保存为standard.jpg

![img](https://gitee.com/chzarles/images/raw/master/imgs/clip_image004.jpg)

​                     																    图2 进行特征点匹配的模板



 

![img](https://gitee.com/chzarles/images/raw/master/imgs/clip_image006.jpg)

​                  图3 校正效果，左边是原图，右边是校正后的图片standard.jpg

## 2.  文字区域截取

得到了校正的图片之后,我们要把文字区域截取出来。

第一步，我根据身份证的文字信息分布特征制作了一张图片(mask.jpg)。可以清晰看见，下左图的空白处正是对应了是身份证的关键信息处。这里我故意将空白区域设计得大一点，下面会讲解原因。

![img](https://gitee.com/chzarles/images/raw/master/imgs/clip_image008.jpg)

​                          图4 特殊图片 mask.jpg

​    第二步, 在程序中读入mask.jpg并转换成和standard.jpg一样的尺寸。

​    第三步, 查找转换后的mask.jpg中的轮廓，并把这些轮廓的坐标点保存下来。因为mask,jpg中的白色区域都是矩形的，而且界限清晰，所以每一次都能找到所有矩形轮廓。又因为mask.jpg的尺寸已经和standard.jpg一致，所以接下来只要用这一步得到的坐标点就能在standard.jpg中裁剪出关键信息

​    第四步,利用第三步得到的坐标点裁剪出区域文字图片，并保持下来。





![img](https://gitee.com/chzarles/images/raw/master/imgs/clip_image010.jpg)

​                    																		图5 截取文字区域图片效果图

 

## 3.  调用百度OCR API识别图片

这步比较简单，只需要在注册一个百度开发者账号，新建一个文字识别的应用，然后看说明文档，学习怎么调用ocr接口就行。最后只要遍历读取识别上面保存的文字区域图片并调用api即可识别出文字。这个api返回的是包含很多信息的字典，所以后续要自己进一步加工信息。





## 4.目录结构

![img](https://gitee.com/chzarles/images/raw/master/imgs/clip_image012.jpg)

​            																			      图6 项目目录结构
