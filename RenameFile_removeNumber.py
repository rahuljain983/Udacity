import os,os.path , sys,re
path = "C:\Rahul\Images"
#This method returns all the directory present in the target path
dirs = os.listdir(path)


for file in dirs:
 if(any(char.isdigit() for char in file)):
     newFile = re.sub(r'\d+', '', file)
     os.rename(os.path.join(path,file),os.path.join(path,newFile))


for file in dirs:
    print(file)

     
     



    

