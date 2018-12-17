import os

file=open("SortModule.txt",'w')
tofile=dir(os)
newfile=str.replace(str(tofile),',','\n')
file.write(str(newfile))
file.close()
