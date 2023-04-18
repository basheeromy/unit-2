# Write a Python program to get a string made of the first 2 and 
# last 2 characters of a given string. If the string length is less than 2, 
# return the empty string instead.

"""
    Sample String : 'w3resource'
    Expected Result : 'w3ce'

    Sample String : 'w3'
    Expected Result : 'w3w3'

    Sample String : ' w'
    Expected Result : Empty String


"""
string = input("Enter the string : ")

def string_partitian(string):
    result = ""
    if len(string) < 2:
        return ""
    else:
        result += string[:2]
        result += string[-2:]
        return result

result1 = string_partitian(string)
print(result1)