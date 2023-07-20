list=["a","b","c","d"]
print(list[0:])
print(list[0:4])
print(list[1:2])

list2=["1","2","3"]
list.extend(list2) #the list copy to other list
print(list)

list.append("fun")#add the values in list
print(list)

list.insert(2,"SELVA")#add the value to the list in desire place by the index number
print(list)

list.remove("1")#remove the value from list
print(list)

#list.clear() #clear the whole list
print(list)

list.remove("a") #remove the value from list
print(list)

list5=["a","b","c","c","a","d"]
print (list5.index("b")) #find the index number of list
print(list5)

list5.pop() #delet the last value from the list
print( list5.count("c")) #how many value in the list by count function


list5.sort() #shot the list by assending number
print(list5)


list5.reverse() #reverse the list
print(list5)

l=list5.copy() #copy the values of one list to others
print(l)

