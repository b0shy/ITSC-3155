#ITSC 3155 Test Commit 1
#Bashar Shabani
#Intro to Python Exercises - Exercise 02

string1 = input('Enter a string: ') #String1 is declared and the user can input a string
string2 = input('Enter another string: ') #String2 is declared and the user can input a string

if string1.endswith(string2) or string2.endswith(string1): #This if-else statement will determine if either string1 or string2 are a suffix of each other
    print("True")
else:
    print("False")