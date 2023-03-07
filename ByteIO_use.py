import io
from PIL import Image
img_url = r'C:\Users\OMEN\Desktop\jpginput\jpg\00000016.dcm_Center_-400_Width_1400.jpg'
with open(img_url, 'rb') as f:
    a = f.read()
print(type(a))
# 将字节对象转为Byte字节流数据,供Image.open使用
byte_stream = io.BytesIO(a)  
print(type(byte_stream))
roiImg = Image.open(byte_stream)  
# 图片保存 
# roiImg.show()
roiImg.save(r'C:\Users\OMEN\Desktop\save.png')