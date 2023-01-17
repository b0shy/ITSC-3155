#ITSC 3155
#Bashar Shabani
#Intro to Python Exercises - Exercise 07

numbers = [] #a list called numbers is created
evenNumbers = [] #a list called evenNumbers is created

while True: #This while-loop continues to ask the user for input until the user inputs QUIT
    userInput = input("Enter a number or QUIT to quit: ")
    if userInput.upper() == "QUIT":
        break
    else:
        number = int(userInput)
        numbers.append(number)
        if number % 2 == 0:
            evenNumbers.append(number)

print("All Nums:", numbers)
print("Even Nums:", evenNumbers)
