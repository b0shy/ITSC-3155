#ITSC 3155
#Bashar Shabani
#Intermediate Python Exercises 1 - script 3

def countLetters(string): #Function will convert string to lowercase, then it will iterate over the function adding each letter to a dict. If it already exists in the dict then 1 will be added to the letter counter of that letter
    letterCount = {}
    for letter in string.lower():
        if letter != " ":
            if letter in letterCount:
                letterCount[letter] += 1
            else:
                letterCount[letter] = 1
    return letterCount

userInput = input("Enter a string: ")
letterCount = countLetters(userInput)
print(letterCount)