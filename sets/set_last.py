# to add a new element to set, we can use set.add() method.

s = {'cat','rat','cow','deer'}

# .copy() method helps us to create copy of a set in source too

c = s.copy()
c.add('jaguar')
print(f"original s is : {s}")
print(f"set c after making copy and add new element is : {c}")

# .set() method also helps to make copy

d = set(s)
print(f"This one is set d : {d}") 

s.add('elephant')
print(s)

s.add('tiger')
print(s)

# to remove an element from set, we can use .remove() method.

s.remove("tiger")
print(s)

# s.remove('mango')

# if we un comment the above given code (s.remove('mango')), 
# as the element 'mango' isn't present in the set s, it will throgh a key error
# to avoid this, we can use .discard(<element>) method. this method also removes element,
# but, if element not present in set, this method quitely does nothing instead of raising an exception

s.discard('mango')
print(s)
s.discard('cow')
print(s)

# .pop()  method removes and returns an randomly chosen element. 
# if set is empty, .pop() method raises an exception:

element = s.pop()
print(element)

# to remove all elements from a set, we can use .clear() method

s.clear()
print(s)