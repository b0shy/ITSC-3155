#ITSC 3155
#Bashar Shabani
#Intermediate Python Exercises 1 - script 2

def getCombinedDict(dict1, dict2): #Function will loop though each key in the first dict and check if it is also in the second dict, only keys in both dicts will be included in the new dict
    combinedDict = {}
    for key in dict1:
        if key in dict2:
            combinedDict[key] = dict1[key] + dict2[key]
    return combinedDict

myDict1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
myDict2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combinedDict = getCombinedDict(myDict1, myDict2)
print(combinedDict)