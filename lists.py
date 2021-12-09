# Create a list using []

a = [1, 2, 3, 45, 43, 56]
 # carefull about sapce 
print(a)
print(a[4]) #index start with 0 1 2 3 4 ....
a[0] = 22  
print(a)



                                     # list are orderd 
b = [45, 'ajay' , False ,4.5]
print(b)
                                     # list slicing
friends = ['ajay', 'tom', 'sajid', 'deep', 'hatim']
print(friends)

print(friends[0:3])
print(friends[-4:]) # when you want last value then use blank[:]
print(friends[:-1])
print(friends[-2:-1])

# var.sort()     sorts the listes  arrenge your values


l1 = [11, 3, 78, 39, 1, 13, 28, 38]
print(l1)
l1.sort()
print(l1)
# var.reverse()  reverse the list
l1.reverse()
print(l1)
# var.append()   add your value in last
l1.append(456)
print(l1)
# var.insert(index,value)
l1.insert(2, 100)
print(l1)
# var.pop            delete element at > index <
l1.pop(0)
print(l1)
# var.remove        remove element from the list
l1.remove(39)
print(l1)
# var.clear          removes all elements 
l1.clear()          
print(l1)


