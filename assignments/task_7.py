# Write a function to remove duplicates from a array

def remove_dup (array):
    set1 = set(array)
    return list(set1)

array = [2,3,3,5,43,3,2,8,7,4]
print(remove_dup(array))