from skimage import io,transform,color
import numpy as np
 
 #图片处理与格式化的函数
def convert_gray(f,**args):
    #读取图片
    rgb=io.imread(f)
    #将彩色图片转换为灰度图片 
    gray=color.rgb2gray(rgb)   
    gray = (gray*255.0).astype('uint8')
    #调整大小，图像分辨率为64*64
    # dst=transform.resize(gray,(64,64)) 
    # dst =  (dst*255.0).astype('uint8')   
    # return dst
    return gray
#图片所在的路径
datapath = r'D:\MatLab高清化\result2月13日\result2'
#识别.jpg的图像
# str=datapath+'/*.jpg'
#识别.png的图像
str=datapath+'/*.png'
#批处理
coll = io.ImageCollection(str,load_func=convert_gray)
#保存图片在d:/input_image4
for i in range(len(coll)):
    io.imsave(r'D:\MatLab高清化\result2月13日\gray'+"\\photo"+np.str(i)+'.jpg',coll[i]) 