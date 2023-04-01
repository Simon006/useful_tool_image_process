from PIL import Image
import os.path
import glob
import cv2

target = r"C:\Users\OMEN\Downloads\horse2zebra\testA\*.jpg"                                  #待转换的文件路径中所有.jpg文件
save_path = r"C:\Users\OMEN\Downloads\horse2zebra\32_testA"                                   #转换格式后的文件存储路径


 
def convertjpg_scale(jpgfile,outdir):  #设置图像缩放规格
    try:
        img = cv2.imread(jpgfile)
        new_img = cv2.resize(img,None,fx=0.2, fy=0.2, interpolation = cv2.INTER_CUBIC)
        cv2.imwrite(os.path.join(outdir,os.path.basename(jpgfile)), new_img)
    except Exception as e:
        print(e)
   



def convertjpg(jpgfile,outdir,width=32,height=32): #设置图像尺寸
    img=Image.open(jpgfile)
    try:
        new_img=img.resize((width,height),Image.Resampling.BILINEAR) 
        new_img.save(os.path.join(outdir,os.path.basename(jpgfile)))
    except Exception as e:
        print(e)


# test
# for jpgfile in glob.glob(target): 
#     convertjpg_scale(jpgfile,save_path)  


for jpgfile in glob.glob(target):  #待转换的文件路径中所有.jpg文件
    convertjpg(jpgfile,save_path)     #转换格式后的文件存储路径