#ITSC 3155
#Bashar Shabani
#Intro to Python Exercises - Exercise 04

n = int(input("Enter a number: ")) #n is declared as an int & the user can input an integer

numberList = [] #a list called numberList is created

for i in range(n): #This for-loop will take the n number of float inputs and store them in the list
    print("Enter number ", i+1 , ":", end=" ")
    numberList.append(float(input()))

print("List:", numberList)

averageNumber = sum(numberList) / len(numberList) #This is where the mean of the list is calculated

print("Average: ", averageNumber)