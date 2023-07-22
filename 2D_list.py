#2D list is define as the list inside the list that can used to store  the number no. of list

list1=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]                                                                          

a=list1[1][2]
b=list1[1][1]

c=a+b
print(c)

for row in list1:
    for col in row:#nestred loop
        print(col)