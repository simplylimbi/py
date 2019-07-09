"""
- have the user input an array
- find the largest value in the array
- print the largest value

~ complex way ~

"""

x = int (input ("how long do you want your array?"))
myArray = [input () for i in range (0,x)]
print (myArray)
y = len(myArray)

result = 0
for i in range (0,y):
    if myArray[i] > myArray[y-1]:
        result = myArray[i]
        i+=1

print (result)
