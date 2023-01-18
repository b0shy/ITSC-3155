#ITSC 3155
#Bashar Shabani
#Intermediate Python Exercises 1 - script 4

def getIntInput():
    while True:
        try:
            return int(input())
        except ValueError:
            print("Invalid input. Please enter an int.")

sum = 0
for integer in range(5):
    print("Enter int #", integer+1, end=": ")
    sum += getIntInput()

print("Your sum is ", sum)