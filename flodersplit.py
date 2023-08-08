import os
import shutil
fromdir="C:/Users/soft5/Downloads"
todir="C:/Users/soft5/Desktop/folder3"
listoffiles=os.listdir(fromdir)
#print(listoffiles)
for file in listoffiles:
    name,ext=os.path.splitext(file)
    #print(name)
   # print(ext)
    if ext=="":
        continue
    if ext in ['.txt', '.doc', '.docx', '.pdf']:
        path1=fromdir+"/"+file
        #newpath=todir+'/'+'imagefiles'
        path3=todir+'/'+file
        shutil.move(path1,path3)
       # print(path1)
       # print(path3)
    # if os.path.exists(newpath):
    #     shutil.move(path1,path3)
    #     print('moving')
    # else:
    #     os.makedirs(newpath)
    #     shutil.move(path1,path3)
    #     print('moving')

    
    