#ITSC 3155
#Bashar Shabani
#Intermediate Python Exercises 1 - script 1

def getUniqueList(lst): #Function will loop through each number in the list and add each unique number to a new list
    uniqueList = []
    for num in lst:
        if num not in uniqueList:
            uniqueList.append(num)
    return uniqueList

myList = [1, 2, 3, 2, 1, 4]
uniqueList = getUniqueList(myList)
print(uniqueList)