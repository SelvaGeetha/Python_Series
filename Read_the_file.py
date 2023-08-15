# Syntex= open=("filename.txt", "comment what can we want to change the file") 
# complusory close the file after open
'''
r=read the file
w=write teh file
a=appent "add the pragraph inlast mode"
r+= read and write 

used function to read and write the file
'''
file=open("read.txt","r")
#print(file.readable())
print(file.readlines()[2]) #print first line
print(file.readline()) #print second line
file.close()