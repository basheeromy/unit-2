# Write a function to check if a given number is prime.

def check_prime(value):
    prime = True
    for i in range(2,int((value/2)+1)):
        if value % i == 0:
            prime = False
            break
    
    return prime   
        
number = int(input("Enter a number : "))        
 
print(check_prime(number))