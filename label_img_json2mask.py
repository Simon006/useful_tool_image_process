
import json
from turtle import shape
import cv2
import matplotlib.pyplot as plt
import numpy as np
 
#对labelme文件的json文件进行生辰mask

dir_path = "D:\\RePaint-main\\data\\datasets\\gts\\face_yang\\"
filename = "yang_mask"
tmp = {}
with open(dir_path+filename+".json", "r") as f:
    tmp = f.read()
 
tmp = json.loads(tmp)
print(tmp["shapes"][0])
points = tmp["shapes"][0]["points"]
points = np.array(points, np.int32)
 
img = cv2.imread(dir_path+filename+".jpg")
#BGR->RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
 
box = tmp["shapes"][1]["points"]
box = np.array(box, np.int32)
 
mask = np.zeros_like(img)
 
cv2.rectangle(img,(box[0][0], box[0][1]), (box[1][0], box[1][1]) ,(125,125,125),2)
#cv2.polylines(img, [points], 1, (0,0,255))
cv2.fillPoly(mask, [points], (255, 255, 255))
img_add = cv2.addWeighted(mask, 0.3,img,0.7,0)
cv2.imwrite(dir_path+"mask.png", mask)
plt.imshow(img_add)
plt.show()
