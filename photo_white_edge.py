
from PIL import Image
import cv2
import math

def add_white_edge(inImgPath, outImgPath, width, height):
    r"""
    给宽图片上下补白边，让其满足一定比例，然后缩放到指定尺寸
    inImgPath: 输入图片路径
    outImgPath: 输出图片路径
    width: 最终宽度
    height: 最终高度
    """
    print("img_path: "+f'{inImgPath}')
    inImg: Image.Image = Image.open(inImgPath)
    bgWidth = inImg.width
    bgHeight = inImg.height
    if bgWidth > bgHeight:
        bgHeight = math.ceil((bgWidth * height) / width)
    # 创建一个白色背景图片    
    bgImg: Image.Image = Image.new("RGB", (bgWidth, bgHeight), (255, 255, 255))        # 同理可以修改为黑点。
    bgImg.paste(inImg, (0, round((bgHeight - inImg.height) / 2)))

    bgImg.resize((width, height), Image.Resampling.LANCZOS).save(outImgPath)

if __name__ == "__main__":
    add_white_edge('C:\\Users\\OMEN\\Desktop\\medical data\\高清胃镜图片\\图片\\106OLCV1\\200H0004.jpg', 'C:\\Users\\OMEN\\Desktop\\test_p1.jpg', 1024+256, 1024+256)