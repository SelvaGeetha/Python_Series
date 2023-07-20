#the function is the group of name that we can assign every where in the python project
#"def" def is used to write the function ,, give name to function ,,":" is used to define the function 
def function_name():
    print("what i want to print")
function_name()
#pass parameter into the function name 
def function_name2():
    a=int(input("enter the number 3:"))
    b=int(input("enter the number 2:"))
    print(a+b)
function_name2()

#def function_name3(c,d):
   # c=int(input("enter the number 3:"))
   # d=int(input("enter the number 2:"))
   # print(max(c,d)+ " lesser than " + min(c,d))
#function_name3()


def function_name3(c,d):
    print(str(c)+ " lesser than " + str(d))
function_name3(23,12)


#must retur the value , when we print return in the function return that line and stop in that line whatever code after return that is not working

def return1(num):
    return num*num+1
print(return1(4))
