# A program to print the Fibonacci series
array = [0,1]
def fibonacci(limit,array):
    i = 1
    while (array[i]+array[i-1]) <= limit :
        array.append(array[i]+array[i-1])
        i += 1
        
limit = int(input("Enter the limit of fibonacci series : "))
fibonacci(limit,array)
print(array)