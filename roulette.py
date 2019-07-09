"""

Roulette Wheel Colors

On a roulette wheel, the pockets are numbered from 0 to 36.
The colors of the pockets are as follows:
- Pocket 0 is green.
- For pockets 1 through 10, the odd-numbered pockets are red
  and the even-numbered pockets are black.
- For pockets 11 through 18, the odd-numbered pockets are black
  and the even-numbered pockets are red.
- For pockets 19 through 28, the odd-numbered pockets are red
  and the even-numbered pockets are black.
- For pockets 29 through 36, the odd-numbered pockets are black
  and the even-numbered pockets are red.
  
Write a program that asks the user to enter a pocket number
and displays whether the pocket is green, red, or black.

The program should display an error message if the user enters a number
that is outside the range of 0 through 36.

"""

# ask the user for a number 0 through 36

pocket = int(input('please enter a pocket number 0 through 36: '))

# even/odd, red or black ?

redBlack = pocket % 2

# display the color of the pocket number chosen

print()

if pocket == 0:
  print('the pocket' , pocket, 'is green.')
elif pocket > 0 and pocket <= 36:
  if pocket >= 1 and pocket <= 10:
    if redBlack == 0:
      print('pocket number' , pocket, 'is black.')
    else:
      print('pocket number' , pocket, 'is red.')
  elif pocket >= 11 and pocket <= 18:
    if redBlack == 0:
      print('pocket number' , pocket, 'is red.')
    else:
      print('pocket number' , pocket, 'is black.')
  elif pocket >= 19 and pocket <= 28:
    if redBlack == 0:
      print('pocket number' , pocket, 'is black.')
    else:
      print('pocket number' , pocket, 'is red')
  elif pocket >= 29 and pocket <= 36:
    if redBlack == 0:
      print('pocket number' , pocket, 'is red.')
    else:
      print('pocket number' , pocket, 'is black.')
else:
  print('sorry, the number is outside of the 0 through 36 range.')
