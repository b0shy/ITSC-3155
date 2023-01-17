#ITSC 3155
#Bashar Shabani
#Intro to Python Exercises - Exercise 06

row = int(input("Enter a row num from 1 to 5: ")) #a variable called row is created where the user can input a number between 1 & 5
col = int(input("Enter a col num from 1 to 5: ")) #a variable called col is created where the user can input a number between 1 & 5

for r in range(1, 6): #for-loop for the rows
    for c in range(1, 6): #for-loop for the columns
        if r == row and c == col: #if-else statement that will determine whether a 1 or 0 is printed
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
