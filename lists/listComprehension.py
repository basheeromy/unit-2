numbers = [1,2,3,4,5,6]

square = [i*i for i in numbers]

print(f"the first list is : {numbers}")
print(f"the second list created from numbers is : {square}")


# here we can do the same with another method called map()
# first, lets see it wih above given way of for loop

cube = [i**3 for i  in numbers]
print(f"Result with for loop : {cube}")

# Now, we are going to do it with map() function 
# First, we have to create a function to calculate cube of the given number

def cubef(number):
    return number**3

# Now, we can create a new list with map function
cube1 = list(map(cubef, numbers))
print(f"Result with map funcion : {cube1}")