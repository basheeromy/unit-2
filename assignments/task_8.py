#  Write a function to calculate the sum of all numbers in a array

def sum_calc(array):
    total = 0
    for i in array:
        total += i
    return total 
        
array = [1,3,44,65,73,89,23]
print(f"sum of all elements from array is : {sum_calc(array)}")