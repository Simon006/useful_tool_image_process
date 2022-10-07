
from urllib.parse import non_hierarchical
import cv2
import numpy as np
from PIL import Image
import matplotlib


def split_512_to_256(path,filename,path_save=''):
    img = Image.open(path)
    img_array = np.array(img)
    img_array_1 = img_array[0:256,0:256]
    img_array_2 = img_array[256:512,0:256]
    img_array_3 = img_array[0:256,256:512]
    img_array_4 = img_array[256:512,256:512]
    print(img_array_1.shape)
    img_array_1 = Image.fromarray(img_array_1)
    img_array_2 = Image.fromarray(img_array_2)
    img_array_3 = Image.fromarray(img_array_3)
    img_array_4 = Image.fromarray(img_array_4)
    
    # img_array_1.save(path_save+filename+'000000.png')
    # img_array_2.save(path_save+filename+'000001.png')
    # img_array_3.save(path_save+filename+'000002.png')
    # img_array_4.save(path_save+filename+'000003.png')
    return list([img_array_1,img_array_2,img_array_3,img_array_4])


def split_photo_mask(path_photo,path_mask):
    split_512_to_256(path_photo,'LR')
    split_512_to_256(path_mask,'mask')
    
path_dir1 = 'D:\\RePaint-main\\data\\datasets\\gts\\LR2HR'
path_dir2 = 'D:\\RePaint-main\\data\\datasets\\gt_keep_masks\\LR2HR'




split_photo_mask(path_dir1+'\\000000.png',path_dir2+'\\000000.png')



