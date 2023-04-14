# an empty set will return false in boolean context
x = set()
print(bool(x))

# we can store any kind of hashable data's in a set, 
# we can't store unhashable datas like list,dict in set
e = {1,"nisam",3.35}
print(e)

"""
    Immutable objects are a type of object that cannot be modified after 
    they were created. Hashable objects, on the other hand, are a type of 
    object that you can call hash() on.
"""
# set methods
# len()
print(len(e))

# in and not in operators

print(1 in e)
print(1 not in e)

# Set union, Given two sets, x1 and x2, 
# the union of x1 and x2 is a set consisting of all elements 
# in either set.

x1 = {'hi','hello','one'}
x2 = {'one','two','three'}

# in python, set union can be achieved with the help of | operator

x3 = x1 | x2
print(x3)

# same can be achieved with .union() method also. 
# the method is invoked on one of the sets, and the other is passed as an argument
x4 = x1.union(x2)
print(x4)

"""
    when we use | operator for set union operation, we have to pass two sets.
    But, in case of .union() method, we can pass any iterable as argument, convert it 
    to set, and performe union operation
"""

l1 = [1,2,2,3,45]
x5 = x1.union(l1)
print(x5)

# to compute union of more than two sets

a = {1,2,3,4,5}
b = {4,5,6,7,8}
c = {"a","b","c","d"}
d = {"87",23,"a",12}

# union of above given sets a,b,c and d with operator

e = a.union(b,c,d)
print(e)

# union of above given sets a,b,c and d with .union method

f = a|b|c|d
print(f)



