import os
from os import  path

#From where the folders want to be create
os.chdir(r'G:\Python\2_mini project\01_Arrange the files\xyz')
def arrange(path):
    files = []
    #It will list the files in the folder
    single_file = os.listdir(path)
    for i in single_file:
        #it will split the file name and extensions
        a=os.path.splitext(i)
        #from the list (a) it will extract the extension 
        #a[1] it specifies the 1st element i the list
        #a[1:] it specifies where to start
        ext=a[1][1:]
        if ext not in files:
            files.append(ext)
    

    for folder in files:
        try:
            #For creating the folders
            os.mkdir(folder)
        except :pass
        for one_file in single_file:
          A= os.path.splitext(one_file)
          if A[1][1:] == folder:
              # It will change the location of the files
              os.rename(os.path.join(path,one_file),os.path.join(folder,one_file))
              
                
if __name__ == "__main__":
    #location of the files
    location=(r"G:\Python\2_mini project\01_Arrange the files\xyz")
    arrange(location)


