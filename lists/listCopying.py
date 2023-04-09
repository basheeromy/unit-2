
list1 = [1]*4
list2 = list1
list2.append('hi')
print(list1)
# here if we print the above given code snippet, 
# we can see that values from list1 also changed when 
# we changed values from list2. it happens because 
# we are only storing address of list in variable. 
# to make an entirely different list, 
# we can choose following ways

list3 = list2.copy()
list3.append('cat')
print(list2)
print(list3)

# we can achieve this with another technique in python with list function

list4 = list(list3)
list4.append('apple')
print(list3)
print(list4)

# we can achieve the same with slicing technique

list5 = list4[:]
list5.append('car')
print(list4)
print(list5)