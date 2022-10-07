import cv2
import numpy as np
from PIL import Image
import matplotlib
#2x2倍图像分辨率掩码生成

# assume image is a numpy array
# im = Image.fromarray(image)
# im.save("1.jpg")



# I = Image.open('./cc_1.png') 
# I.show()    
# I.save('./save.png')
# I_array = np.array(I)



def img_to_nparray(path,ifprint=False):
    img = Image.open(path)
    #img.show()
    img_array = np.array(img)
    if ifprint==True:
        img.show()
    #print(img_array)
    return img,img_array




## start to transform
img_path = "D:\\RePaint-main\\test.png"
img,img_np = img_to_nparray(img_path)



# print(type(img_np))
# print(type(img_np.shape[0]))

# print(len(np.linspace(1,30,5)))




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


img_scaler_np,mask = nparray_scaler_and_mask(img_np)  


img_scaler = Image.fromarray(uint_nparray(img_scaler_np))

img_mask = Image.fromarray(uint_nparray(mask))

# img_scaler.show()
# img_mask.show()



img_mask.save('mask.png')
img_scaler.save('img_scaler.png')


# print(mask[0,0,1])
# print(type(img_scaler_np))
# print(img_scaler.shape)
# print(img_np.shape)



