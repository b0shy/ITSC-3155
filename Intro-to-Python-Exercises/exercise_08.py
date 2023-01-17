#ITSC 3155
#Bashar Shabani
#Intro to Python Exercises - Exercise 08

numbers = [] #a list called numbers is created

for i in range(10): #for-loop that will take in 10 integers from the user
    print("Enter number ", i+1, ":", end=" ")
    numbers.append(int(input()))

uniqueNumbers = [] #a list called uniqueNumbers is created
for number in numbers: #this for-loop will check for numbers that appear only once
    if numbers.count(number) == 1:
        uniqueNumbers.append(number)

print("Original list: ", numbers)
print("Nums that appear once: ", uniqueNumbers)
