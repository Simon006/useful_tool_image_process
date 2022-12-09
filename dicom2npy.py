import numpy as np
import os
import pydicom

'''
本程序可以将path1内的所有dicom文件夹内的dicom文件分别放到不同的npy数据中，
并存入目标path2
'''


# N 是需要处理的dcm文件总量
path1 = r'D:\LUNG-LIDC\test_data_1'
path2 = 'images'
files = os.listdir(path1)
N = len(files)
W = 512
H = 512

if not os.path.exists(path2):
    os.makedirs(path2)

# print(files[4][-3:]) 

count = 0
for n in range(len(files)):
    if os.path.isdir(os.path.join(path1,files[n])):
        count+=1

    volumeID = '{:0>4}'.format(count)
    print('Processing File ' + volumeID)
    filename1 = files[n]
    directory1 = os.path.join(path1, filename1)
    filename2 = volumeID + '.npy'
    #os.walk返回三个值 root 所指的是当前正在遍历的这个文件夹的本身的地址 dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录) files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)
    for path_, _, file_ in os.walk(directory1):
        L = len(file_)
        if L > 0:
            print('  ' + str(L) + ' slices along the axial view.')
            data = np.zeros((W, H, L), dtype = np.int16)
            for f in sorted(file_):
                #返回绝对路径
                if f[-3:]=='dcm':
                    file1 = os.path.abspath(os.path.join(path_, f))
                    image = pydicom.read_file(file1,force=True)
                    sliceID = image.data_element("InstanceNumber").value - 1
                    if image.pixel_array.shape[0] != 512 or image.pixel_array.shape[1] != 512:
                        exit('  Error: DICOM image does not fit ' + str(W) + 'x' + str(H) + ' size!')
                    data[:, :, sliceID] = image.pixel_array
                else:
                    continue
                
            file2 = os.path.join(path2, filename2)
            np.save(file2, data)
            print('File ' + volumeID + ' is saved in ' + file2 + ' .')