# Write a program to find the maximum and minimum   elements in an array of integers.

def find_max_min(array):
    max_element = array[0]
    min_element = array[0]
    for i in array:
        if i > max_element:
            max_element = i 
        elif i < min_element:
            min_element = i 
    return max_element, min_element


array = [12,43,8,3,2,56,33,22,1,569]
maxel, minel = find_max_min(array)
print(maxel)
print(minel)