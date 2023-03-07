import matplotlib.pyplot as plt
import pydicom
import pydicom.uid
import sys
import PIL.Image as Image
from PyQt5 import QtGui
import os
from dicom2jpg import *

#存放DICOM文件的文件夹path

# image_path1 = "D:\\MatLab高清化\\超清化原图2022-10-27\\超清化原图2022-10-26\\wangxingrong"
# image_path2 = "D:\\MatLab高清化\\超清化原图2022-10-27\\超清化原图2022-10-26\\zhaofei"
image_path1 = r"C:\Users\OMEN\Desktop\jpginput\DCM"
# img_path_dir =[image_path1,image_path2,image_path3] 
img_path_dir = [image_path1]



#定义预读的图片文件类型
img_type = ['.jpg','.JPG','.png','.PNG','.bmp','.BMP','.dcm',"ima","IMA"]    # 可继续添加图片类型
def image_compose(image_path):
    if not os.path.isdir(image_path):
        return -1
    imgpath_vec = [os.path.join(image_path,imgpath) for imgpath in os.listdir(image_path) if os.path.splitext(imgpath)[1] in img_type]
    return imgpath_vec
    


# imgpath_vec = image_compose(image_path=image_path2)
# print(imgpath_vec)


def dicom_batch_to_jpg(file_path_dir,path_out_dir=os.getcwd(),WindowCenter=None,WindowWidth=None):
    n_dir = len(file_path_dir)
    for i in range(n_dir):
        image_path = file_path_dir[i]
        filename = [imgpath for imgpath in os.listdir(image_path)]
        imgpath_vec = image_compose(image_path=image_path)
        for j in range(len(imgpath_vec)):
            #使用时请确保输入成对窗宽和窗位
            if WindowCenter==None:
                information = loadFileInformation(imgpath_vec[j])
                WindowCenter = information['WindowCenter']
                WindowWidth = information['WindowWidth']
                print('WindowCenter={},WindowWidth={}'.format(WindowCenter,WindowWidth))
            
            information = loadFileInformation(imgpath_vec[j])
            information['WindowCenter'] = WindowCenter 
            information['WindowWidth'] = WindowWidth
            
            dcm = pydicom.dcmread(imgpath_vec[j])  # 加载Dicom数据
            img_data = get_pixeldata(dcm)[0]
            img_temp = setDicomWinWidthWinCenter(img_data,WindowWidth, WindowCenter, get_pixeldata(dcm)[1],get_pixeldata(dcm)[2])
            dcm_img = Image.fromarray(img_temp)  # 将Numpy转换为PIL.Image
            dcm_img = dcm_img.convert('L')
            

            # 保存为jpg文件，用作后面的生成label用
            dcm_img.save(path_out_dir+'\\'+filename[j]+"_Center_"+str(WindowCenter)+"_Width_"+str(WindowWidth)+'.jpg')
            # 显示图像
            # dcm_img.show()


path_out_dir = "C:\\Users\\OMEN\\Desktop\\result1"
dicom_batch_to_jpg(img_path_dir,path_out_dir,-400,1400)