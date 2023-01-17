#ITSC 3155
#Bashar Shabani
#Intro to Python Exercises - Exercise 05

firstList = [] #a list called firstList is created

for i in range(5): #for-loop that will take in the users input of 5 integer and store them in the firstList
    firstList.append(int(input("Enter a number for the first list: ")))

secondList = [] #a list called firstList is created

for i in range(5): #for-loop that will take in the users input of 5 integer and store them in the secondList
    secondList.append(int(input("Enter a number for the second list: ")))

commonList = list(set(firstList) & set(secondList)) #a third list is created called commonList, this list will store the common integers from the previous lists

print("First List: ", firstList)
print("Second List: ", secondList)
print("Common List: ", commonList)