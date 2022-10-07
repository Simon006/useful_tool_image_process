
import os
import cv2
import numpy as np
import PIL.Image as Image
import matplotlib.pyplot as plt
 
img_type = ['.jpg','.JPG','.png','.PNG','.bmp','.BMP']#可继续添加图片类型
 
#把文件夹下的图片全部拼接成一张大图


#输入几行几列
ROW = 5
COL = 5
 
def resize_blank_img(srcimg, dstpath):
    img = cv2.imread(srcimg)
    blankimg = np.zeros(np.shape(img), np.uint8)
    blankimg[:, :, 0] = 255
    blankimg[:, :, 1] = 255
    blankimg[:, :, 2] = 255
    num = [os.path.join(dstpath,imgpath) for imgpath in os.listdir(dstpath) if os.path.splitext(imgpath)[1] in img_type]
    cv2.imwrite(dstpath + "\\" + str(len(num)+1) + ".jpg", blankimg)
 
def image_compose(image_path):
    if not os.path.isdir(image_path):
        return -1
    imgpath_vec = [os.path.join(image_path,imgpath) for imgpath in os.listdir(image_path) if os.path.splitext(imgpath)[1] in img_type]
    # print(imgpath_vec)
    # print(imgpath_vec[0])
    # print(len(imgpath_vec))
 
    #1、使用平均的width，heigth或者可以自定义width，heigth
    avg_width = 0
    avg_heigth = 0
    if avg_width == 0 or avg_heigth == 0:
        size = []
        for item in imgpath_vec:
            size.append((Image.open(item)).size)
        sum_width = sum_heigth = 0
        for item in size:
            sum_width += item[0]
            sum_heigth += item[1]
        avg_width = int(sum_width/(len(size)))
        avg_heigth = int(sum_heigth/(len(size)))
    avg_size = (avg_width,avg_heigth)
 
    #2、resize图片大小
    vec = [os.path.join(image_path, imgpath) for imgpath in os.listdir(image_path) if
           os.path.splitext(imgpath)[1] in img_type]
    while (len(vec)) < COL * ROW:
        vec = [os.path.join(image_path, imgpath) for imgpath in os.listdir(image_path) if
                       os.path.splitext(imgpath)[1] in img_type]
        resize_blank_img(vec[0],image_path)
 
    imgs = []
    for item in vec:
        imgs.append((Image.open(item)).resize(avg_size,Image.Resampling.BILINEAR))
 
    #3、拼接成大图
    result_img = Image.new(imgs[0].mode,(avg_width * COL,avg_heigth * ROW))
    index = 0
    #注意先行后列还是先列后行
    for j in range(COL):
        for i in range(ROW):
            result_img.paste(imgs[index],(i * avg_width, j * avg_heigth))
            index+=1
 
    #4、显示拼接结果
    plt.imshow(result_img)
    plt.show()
    # result_img.save('synthesis.png')
    # result_img.save(path)#保存结果
 
if __name__ == "__main__":
    path = r'D:\\RePaint-main\\log\\polyp_test3\\inpainted'#输入你的图片路径
    image_compose(path)
