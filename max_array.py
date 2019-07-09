"""
- have the user input an array
- find the largest value in the array
- print the largest value
"""

# how long do you want your array

x = int (input ("how long do you want your array?"))

myArray = [input () for i in range (0,x)]

# print and display the largest value

print (myArray)

print (max (myArray))

