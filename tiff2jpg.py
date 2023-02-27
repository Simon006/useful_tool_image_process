import cv2.cv2 as cvtool

import os


path = r"C:\Users\OMEN\Desktop\result1"
tif_list = [x for x in os.listdir(path) if x.endswith(".tif")]   # 获取目录中所有tif格式图像列表
for num,i in enumerate(tif_list):      # 遍历列表
    img = cvtool.imread(i,-1)       #  读取列表中的tif图像
    cvtool.imwrite(i.split('.')[0]+".jpg",img)    # tif 格式转 jpg 并按原名称命名
    print("success",i)


# # 批量tiff转jpg
# # 代码中路径更改为自己图像存放路径即可
# from PIL import Image
# import os
 
# imagesDirectory = r"C:\Users\OMEN\Desktop\result1"  # tiff图片所在文件夹路径
# distDirectory = r"C:\Users\OMEN\Desktop\result1"# 要存放jpg格式的文件夹路径
# for imageName in os.listdir(imagesDirectory):
#     imagePath = os.path.join(imagesDirectory, imageName)
#     image = Image.open(imagePath)# 打开tiff图像
#     distImagePath = os.path.join(distDirectory, imageName[:-4]+'.jpg')# 更改图像后缀为.jpg，并保证与原图像同名
#     print(imagePath)
#     image.save(distImagePath)# 保存jpg图像