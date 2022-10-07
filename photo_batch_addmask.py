import cv2
import numpy as np
import os
 
pic_path = 'C:\\Users\\OMEN\\Desktop\\test_p1.jpg' # 分割的图片的位置
pic_target = 'C:\\Users\\OMEN\\Desktop\\result\\' # 分割后的图片保存的文件夹
if not os.path.exists(pic_target):  #判断是否存在文件夹如果不存在则创建为文件夹
    os.makedirs(pic_target)

#定义预读的图片文件类型
img_type = ['.jpg','.JPG','.png','.PNG','.bmp','.BMP']    # 可继续添加图片类型

#读取文件嘉路径下的所有图片
def image_compose(image_path):
    if not os.path.isdir(image_path):
        return -1
    imgpath_vec = [os.path.join(image_path,imgpath) for imgpath in os.listdir(image_path) if os.path.splitext(imgpath)[1] in img_type]
    # print(imgpath_vec)
    


#要分割后的尺寸
cut_width = 256
cut_length = 256
# 读取要分割的图片，以及其尺寸等数据
picture = cv2.imread(pic_path)
(width, length, depth) = picture.shape
# 预处理生成0矩阵
pic = np.zeros((cut_width, cut_length, depth))
# 计算可以划分的横纵的个数
num_width = int(width / cut_width)
num_length = int(length / cut_length)
# for循环迭代生成
for i in range(0, num_width):
    for j in range(0, num_length):
        pic = picture[i*cut_width : (i+1)*cut_width, j*cut_length : (j+1)*cut_length, :]      
        result_path = pic_target + '{}_{}.jpg'.format(i+1, j+1)
        cv2.imwrite(result_path, pic)
 
print("done!!!")