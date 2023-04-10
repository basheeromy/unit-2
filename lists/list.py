# this file is to practice list in python

# declare a list of fruits
fruits = ['mango','apple','orange','kiwi','water melon','lemon']

# print 0 th value in fruits list
print(fruits[0])

# check a value is present in a list or not
if "car" in fruits:
    print('yes it is there')
else:
    print("no it's not available")
# print last value in list fruits by using negetive indexing technique also use f string (formated string) syntax 
print(f"we can access last element in python list with -1 index and it is : {fruits[-1]}")

# add a new value to list by using append method of python list as the last value of list
fruits.append('jackfruit')
print(fruits)

# using insert method of python list, insert a value to desired index: here we are inserting value to 3rd index position.
fruits.insert(3,'pine apple')
print(fruits)

# using pop method of python lists, we can take last item of python list and delete it at same time.
take = fruits.pop()
print(fruits)
print(f"we took the last value out of the list and assigned to a variable called take by using pop method and the value is : {take}")

# using pop by giving index as an argument to change default behaviour
take = fruits.pop(2)
print(fruits)
print(f'removed and assigned another value by giving index to pop method and removed value is : {take}') 

# remove an item from python list by using remove method
fruits.remove('water melon')
print(fruits)

# remove all items in the list by using clear method
fruits.clear()
print(f"an empty list {fruits}")

print('practise zone')

cars = [1,2,3,4,5]
trucks = [i*3 for i in cars ]
print(trucks)

# we can assing a range of values to an array with the  help of range funciton
# arguments passed are, start point, end point, interval
numerics = list(range(0,9,2))
print(numerics)