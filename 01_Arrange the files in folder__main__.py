import os
from os import  path
os.chdir(r'X:\Python\xyz')
def arrange(path):
    files = []
    single_file = os.listdir(path)
    for i in single_file:
        a=os.path.splitext(i)
        ext=a[1][1:]
        if ext not in files:
            files.append(ext)
    print(files)
    

    for folder in files:
        try:
            os.mkdir(folder)
        except :pass
        for one_file in single_file:
          A= os.path.splitext(one_file)
          if A[1][1:] == folder:
              os.rename(os.path.join(path,one_file),os.path.join(folder,one_file))
                
if __name__ == "__main__":
    location=(r"X:\Python\xyz")
    arrange(location)


