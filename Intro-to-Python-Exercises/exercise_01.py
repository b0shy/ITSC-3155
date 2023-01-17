#ITSC 3155
#Bashar Shabani
#Intro to Python Exercises - Exercise 01

grade = int(input('Enter a grade from 0 to 100: ')) #Statement where grade is initialized as an int variable & where the user will input their grade

if(grade < 60): #if-else statement to determine the users grade based on their input
    print('Your grade is F')
elif(grade >= 60 and grade <= 69):
    print('Your grade is D')
elif(grade >=70 and grade <=79):
    print('Your grade is C')
elif(grade >= 80 and grade <= 89):
    print('Your grade is B')
elif(grade >= 90 and grade <= 100):
    print('Your grade is A')
else:
    print('Invalid Input: Please Enter a grade from 0 to 100: ')