# sets are another built in data type in python
# sets are used to store multiple items in a single variable
# duplicate values can't store in sets and sets are unordered
# we can initiate a set in multiple ways, with set syntax
sets = {1,2,3,4}
print(sets)

# with set function, we can pass either tuple or list or string etc..
a = set([1,2,3,4,5])
print(a)
print(type(a))

b = 'welcome'
c = set(b)
print(c)
# each time we can see that the elements in resultant set is in different order 
# but, if we try to convert the same with list, we can see the resultant list has order and it contains duplicate elements
d = list(b)
print(d)

# we can initiate an empty set, but, by default, python interpret empty
# curly braces as an empty dictionary. so, we have to use set function to define an empty set

e = set()
print(type(e))

