# this file is the second file for practicing list method in python

numbers = [1,2,3,4,5,5,6,6,7,7,48,-3,0,0.5]

# reverse the order of list with reverse method
numbers.reverse()
print(numbers)

# sort list in ascending order with the help of sort method
numbers.sort()
print(numbers)

# sort the list in descending order
numbers.sort(reverse=True)
print(numbers)

# we can reverse and assign the list in another way

list3 = numbers[::-1]
print(f"reversed list with steps and elements are :  {list3}")

# sort list of letters and strings
letters = ['c','d','f','g','a','c','b','bat','ball','bali']
letters.sort()
print(letters)

# assing a list as sorted to new variable

orderly = sorted(letters)
print(orderly)

# create a list with multiple identical values
list_1 = [1] * 8
print(list_1)

