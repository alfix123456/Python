'''In this program we will test openning files
in python
'''
file=open("testfile.txt",'r')
file.seek(0)
filecontent=file.readlines()
content=[i.rstrip("\n") for i in filecontent ]



'''filecontent=file.read()
'''
#print(filecontent)
print(content)
file.close()
