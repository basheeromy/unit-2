import sys
import timeit

# initialize a variable and assign a tuple as value
myTuple = ('mango', 1, 'max','car','truck','place','name')

# print an item from tuple using index
print(myTuple[2])
# print an item from tuple using negetive index
print(myTuple[-4])

# check an item present in tuple or not
if 'mango' in myTuple:
    print('yes')
else:
    print('no')
    
    
"""
assign value from one tuple to another one
here we are giving four as end value of index referece, 
but as this process will only check until less than the given upper limit, 
this will not throw any errors
"""

secondTuple = myTuple[1:4]
print(f"the second tuple is : {secondTuple}")

thirdTuple = myTuple[::2]
print(thirdTuple)


# As tuples are immutable, we can't sort or change a tuple. 
# so, instead of sorting the tuple with sort() method, we can create a new
# sorted tuple or list with the help of sorted function
# sorted function will return a list, so, we can convert them into tuple by tuple() function

numbers = (9,5,3,1,2,5,7,2,3,5,1,0)
ascend = tuple(sorted(numbers))
print("data type : ",(type(ascend))," the sorted tuple is : ",ascend)

# to check length of tuple
print(len(numbers))

# to get count of an element in tuple 
print(numbers.count(5))

# to get index of a particular element in a tuple
print(numbers.index(5))

# we can make a list out of tuple
my_list = list(numbers)
print(my_list)

# also we can convert a list to tuple
my_tuple = tuple(my_list)

# we can assign values from tuple to variables in an easy way

student = 'basheer', 26, 'kozhikode', 'kerala' 
name,age,distict,state = student
print(state)
# here, we have to assign all elements in this operation, 
# otherwise we will get value error, too many values to unpack
# if we just want to assign only a few elements, we have to choose other ways
# un comment the bellow given codes to see that error
"""
name1, age1 = student
print(name1)
"""

# we can take desired values from tuple like this , 
# if we assign other remaining values to  a variable with star at beginning, 
# this will return a list and we will get other values in variables
numerics = (1,22,3,4,5,6,7)
i1, i2, *i3, i4,i5 = numerics
print(i3)

# Compare list with tuple

Clist = [0,1,2,"hello","cat"]
Ctuple = (0,1,2,"hello","cat")
print(sys.getsizeof(Clist), "bytes")
print(sys.getsizeof(Ctuple), "bytes")

# working with tuple can be more efficient than working with list
# let's check the time difference to perform with list and tuple, this one also proves that tuple is more efficient

print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000))

# let's try to assing data with the help of range function

sample = tuple(range(0,6,1))
print(f"tuple created with the help of range function is : {sample}")