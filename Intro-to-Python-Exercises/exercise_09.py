#ITSC 3155
#Bashar Shabani
#Intro to Python Exercises - Exercise 09

words = [] #a list called words is created

for i in range(5): #for-loop where the user will be able to enter 5 words, and the words will then be put together to create a single string
    word = input("Enter a word: ")
    words.append(word)
    
string = " ".join(words)
print("Words: ", words)
print("One String: ", string)
