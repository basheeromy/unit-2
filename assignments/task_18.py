# Write a program to find the union of two arrays of integers.

# The union of two arrays: is the set of all elements that are either in A or in B without duplictes

array1 = [1,2,4,5,34,5,6,2,1,3,4]
array2 = [2,36,87,2,3,3,9,98,0]

# merge two arrays
array3 = array1 + array2

# sort two arrays
array3.sort()

# remove duplicates
i = 1
while i < len(array3):
    if array3[i-1] == array3[i]:
        array3.remove(array3[i])
        i -= 1
    i += 1

print(array3)
    