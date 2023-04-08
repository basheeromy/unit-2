# we can take values from a list with the bellow given method

mylist = [1,2,3,4,5,6,7,8,9]

secondlist = mylist[2:6]
# use [:5] to take values from 0th index to five
# use [2:] to take all items from 2nd index to end 
print(secondlist)

# to iterate with indexes in different way, use step 
# here we are skipping one element

thirdlist = mylist[::2]
print(thirdlist)

