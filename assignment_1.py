"""

1. ask for students name
2. ask the user for a total of 10 test scores, ranging from 0 - 100
3. evaluate the test scores and determine the students grade as a percentage
4. print out a statement that includes the students name and grade
5. optional, print students letter grade

"""

# ask for their name

name = input ("hey there, whats your name? ")

print ("nice to meet you" , name, "\n" "i'd like to know what your last 10 test scores were")

# student enters scores

test1 = float (input ("first test: "))
test2 = float (input ("2nd test: "))
test3 = float (input ("3rd test: "))
test4 = float (input ("4th test: "))
test5 = float (input ("5th test: "))
test6 = float (input ("6th test: "))
test7 = float (input ("7th test: "))
test8 = float (input ("8th test: "))
test9 = float (input ("9th test: "))
test10 = float (input ("finally, last but not least: "))

# calculate the average

average = (test1 + test2 + test3 + test4 + test5 + test6 + test7 + test8 + test9 + test10) / 10.0
avgAgain = average / 100.0

print ("yay!" , "so," , name , "your average is:", (format (avgAgain, '2.2%')))

# name the letter

gradeA = 90
gradeB = 80
gradeC = 70
gradeD = 60
superFail = 50

# determine the grade

if average >= gradeA:
    print ("congrats! you got an 'a'!")
else:
    if average >= gradeB:
        print ("not bad, your grade is a 'b'")
    else:
        if average >= gradeC:
            print ("okay, your grade is a 'c'")
        else:
            if average >= gradeD:
                print ("what are you doing? your grade is a 'd' ...")
            else:
                if average <= superFail:
                    print ("yeah, you failed...")
