#ITSC 3155
#Bashar Shabani
#Intro to Python Exercises - Exercise 10

string = input("Enter a string: ") #a variable called string is created wherte the user will be able to enter a string
characters = list(string) #the string will be converted into a list of characters here

characterLists = [characters[n:n+3] for n in range(0, len(characters), 3)] #this is where the characters will be split into a list of lists where each inner list has only 3 elements

print(characterLists)
