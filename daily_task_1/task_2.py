# Write a Python program to add 'ing' at the end of a given string (length should be 
# at least 3). If the given string already ends with 'ing', add 'ly' instead. If the 
# string length of the given string is less than 3, leave it unchanged.

"""
    Sample String : 'abc'
    Expected Result : 'abcing'

    Sample String : 'string'
    Expected Result : 'stringly'
"""

string = input("Enter the string : ")

def modify_string(string):
    if len(string) >= 3:
        if string[-3:] == "ing":
            string += "ly"
        else:
            string += "ing"

    return string

result = modify_string(string)
print(result)