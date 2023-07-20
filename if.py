a= True
b= False
if b:
    print("a")
elif a and b:
    print("a and b")
elif a and not(b):
    print("a and not b") 
elif b and not(a):
    print("b and not a") 
else:
    print("not a and b")