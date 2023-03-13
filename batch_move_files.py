import os
import shutil
 
#想要移动文件所在的根目录
rootdir=r"C:\Users\OMEN\Downloads\TrainValid\TrainValid\Images"
#获取目录下文件名清单
list=os.listdir(rootdir)
#print(files)
#目标路径
des_path_root = r"D:\息肉图片汇总\polyps"


#移动图片到指定文件夹
for i in range(0,len(list)):     #遍历目录下的所有文件夹
	path=os.path.join(rootdir,list[i])    
	if os.path.isdir(path):		 #判断是否为文件夹
		for item in os.listdir(path): #遍历该文件夹中的所有文件
			dirname=os.path.join(rootdir,list[i]) #将根目录与文件夹名连接起来，获取文件目录
			full_path=os.path.join(dirname,item) #将文件目录与文件名连接起来，形成原来完整路径
			des_path = os.path.join(des_path_root,list[i]+"_"+item)   # 避免文件同名的时候出错
			shutil.move(full_path,des_path)  #移动文件到目标路径
			print(full_path)
			print(des_path)	