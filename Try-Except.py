#some time the user enter the value the simplification that time the user was enter the some alphet letter at that time the programer should give the message

try:
    value=1543/0
    a=int(input("enter the Value:"))
    print(a)
except ZeroDivisionError:
    print("divide by zero")
except ValueError:
    print("invalid")


#we put more exception value to print 

