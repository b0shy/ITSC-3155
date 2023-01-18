#ITSC 3155
#Bashar Shabani
#Push Module 1 to GitHub + More Python Exercises - Exercise 2

userString = input("Enter a string: ") #userString is declared where the user can input a string

lowerCase = [] #a list called lowerCase is created
upperCase = [] #a list called upperCase

for char in userString: #This for-loop will seperate the lower and upper case letters
    
    if char.islower():
        lowerCase.append(char)
    elif char.isupper():
        upperCase.append(char)

shiftedString = ''.join(lowerCase) + ''.join(upperCase) #This will organize the letters in order from lower case and upper case
print(shiftedString)