# Write a function to calculate the factorial of a given number n


def find_factorial(number):
    factorial = 1
    for i in range (1,number+1):
        factorial *= i
    return factorial

number = int(input("Enter the value to find factorial : "))
print(find_factorial(number))
