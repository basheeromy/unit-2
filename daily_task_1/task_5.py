# Write a Python program to replace the last value of tuples in a list.

""" 
    Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
    Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

"""

list1 = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
list2 = []
for i in list1:

    tuple1 = i[:-1] + (100,)
    list2.append(tuple1)
    
print(list2)