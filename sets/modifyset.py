"""
    Although the elements contained in a set must be of immutable type, 
    sets themselves can be modified. Like the operations above, 
    there are a mix of operators and methods that can be used to 
    change the contents of a set.
"""

# .add() method, this method takes only one argument

myset = set()
myset.add(1)
myset.add("b")
myset.add(("calicut","kerala",5))
print(myset)

# .remove() method, this method will throw error if we give key which isn't present in the set

myset.remove(1)
print(myset)

# .discard() method, this method also do the same like remove, but, if the key isn't present, it will not through any error

myset.add(3)
print(myset)
myset.discard(7)
myset.discard(3)
print(myset)

# .pop() method, this method is used to take a value out of the set

a = myset.pop()
print(a)
print(myset)


# .update method, this method is used to update the set

secondset = {"cat","rat","bat"}
myset.update(secondset)
print(myset)

# do the same updation with operators
thirdset = {1,2,3,4,5,"cat"}

myset |= thirdset
print(myset)
# .clear() method, this method is used to empty the set
myset.clear()
print(myset)

# .intersection_update() method retaining only elements found in both sets

set1 = {"cat","rat","cow","goat"}
set2 = {"deer","cat","cow"}

set2.intersection_update(set1)
print(set2)

# intersection update with operators

x1 = {1,2,3,4,5}
x2 = {3,4,5,6,7}

x1 &= x2
x3 = x1 & x2
print(x1)
print(x3)

# difference_update() method removes elements found in comparing set.

x4 = {"kozhikode","kannoor","malappuram","wayanad","thrissure"}
x5 = {"thrissure","wayanad"}

x4.difference_update(x5)
print(x4)
# the above given difference_update method can achive with -= operator too

x6 = {1,2,3,4,5,6}
x7 = {5,6,7,8}

x6 -= x7
print(x6)

x6 = {1,2,3,4,5,6}
x8 = x7 - x6
print(x8)

# .symmetric_difference_update() method retains elements found in either , but not both.

x9 = {'tiger','lion','cat','squirrel'}
x10 = {'cat','tiger','deer','puma'}
x11 = {'lion','mango','apple'}

x9.symmetric_difference_update(x10)
print(x9)
x9 ^= x11
print(x9)