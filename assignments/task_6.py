# Write a function to find the second largest number in a array

def find_second_largest(array):
    array.sort()
    return array[-2]

array =  [1,3,2,56,3,45,7,100]
print(f"second largest element in array is : {find_second_largest(array)}")