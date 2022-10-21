import os
from PIL import Image
import numpy as np
import cv2
import matplotlib
#2x2倍图像分辨率掩码生成



dir_path = "D:\\RePaint-main\\polyp_data_test"


def img_to_nparray(path,ifprint=False):
    img = Image.open(path)
    #img.show()
    img_array = np.array(img)
    if ifprint==True:
        img.show()
    #print(img_array)
    return img,img_array

# input a np.array() object
def nparray_scaler_and_mask(nparray):
    x = nparray.shape[0]
    y = nparray.shape[1]
    #print(x)
    img_scaler_np = np.zeros([2*x,2*y,3])
    k = np.linspace(0,2*x,x)
    j = np.linspace(0,2*y,y)
    # print("k",k)
    # print("x:",x)
    assert(len(k)==x)
    assert(len(j)==y)
    img_scaler_np[::2,::2] = nparray[:,:,0:3]
    mask = np.zeros_like(img_scaler_np)
    mask[img_scaler_np>0]=255
    return img_scaler_np,mask


def uint_nparray(nparray):
    return np.uint8(nparray)


def dir_to_2x2_image_mask(dir_path):
    img_type = ['.jpg','.JPG','.png','.PNG','.bmp','.BMP']
    if not os.path.isdir(dir_path):
        return -1
    imgpath_vec = [os.path.join(dir_path,imgpath) for imgpath in os.listdir(dir_path) if os.path.splitext(imgpath)[1] in img_type]
    # print(imgpath_vec)
    # print(imgpath_vec[0])
    # print(len(imgpath_vec))
    for i in range(len(imgpath_vec)):
        img,img_np = img_to_nparray(imgpath_vec[i])
        img_scaler_np,mask =  nparray_scaler_and_mask(img_np)
        img_scaler = Image.fromarray(uint_nparray(img_scaler_np))
        img_mask = Image.fromarray(uint_nparray(mask))
        img_scaler.save(dir_path+"\\img_scaler_"+str(i)+".png")
        img_mask.save(dir_path+"\\img_mask_"+str(i)+".png")


dir_to_2x2_image_mask(dir_path)
