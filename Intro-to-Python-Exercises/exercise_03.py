#ITSC 3155
#Bashar Shabani
#Intro to Python Exercises - Exercise 03

integer1 = int(input("Enter an integer greater than 1: ")) #integer1 is declared as an int & the user can input an integer

for i in range(integer1 + 1): #This for-loop calculates the cube of the current value in the itteration using the i**3 line. 
    
    cube = i**3
    
    print("The cube of ", i, " is ", cube)

