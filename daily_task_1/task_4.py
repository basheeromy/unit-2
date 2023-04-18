# Write a Python program to find the length of a given list of non-empty strings.

"""
    Input:
    ['cat', 'car', 'fear', 'centre']

    Output:
    [3, 3, 4, 6]

    Input:
    ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']

    Output:
    [3, 3, 7, 5, 2, 4, 0]

"""
animals = ['cat','lion','tiger','elephant','cheetah']

length = []

for i in animals:
    length.append(len(i))

print(animals)
print(length)