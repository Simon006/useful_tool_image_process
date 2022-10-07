
from PIL import Image
import numpy as np
import cv2

filename = 'label.png'
path = 'D:\\image pre process'
def numpy2img(image,filename):
    image_out = Image.fromarray(image)
    image_out.save(filename+'.png')
    return image_out



I = Image.open('C:\\Users\\OMEN\\Desktop\\img_json\\label.png') 
I.show()    
#去除除了0和255的值
I_array = np.array(I)
I_array[I_array>0] = 255
I_array[I_array<255] = 0
I_array0 = ~I_array 

numpy2img(I_array0,filename)
print(I_array.shape)

def read_img_shape(path):
    img = cv2.imread(path)
    size = img.shape
    print(size)


'''
read_img_shape('D:\\RePaint-main\\data\\datasets\\gt_keep_masks\\face_zhong\\000000.png')
print('next')
read_img_shape('D:\\RePaint-main\\data\\datasets\\gt_keep_masks\\face_yang\\000000.png')
'''