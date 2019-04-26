# Write a program to perform following operations on List.
# Create three lists as List1, List2 and List3 having 5 city names each list.

def getKeysByValue(dictOfElements, valueToFind):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item in listOfItems:
        if item[1] == valueToFind:
            listOfKeys.append(item[0])
    return listOfKeys[0]


city1 = ["Delhi", "Mumbai", "Kolkata", "Chennai", 'Bangalore']
city2 = ['Moradabad', 'Ghaziabad', 'Bhopal', 'Noida', 'Greater Noida']
city3 = ['Combaitore', 'Mysore', 'Hyderabad', 'Vellore', 'Gurgaon']

d1 = dict()
d2 = dict()
d3 = dict()

# a. Find the length city of each list element and print city and length

for i in range(0, 5):
    d1[city1[i]] = len(city1[i])
    d2[city2[i]] = len(city2[i])
    d3[city3[i]] = len(city3[i])

print(d1)
print(d2)
print(d3)

# b. Find the maximum and minimum string length element of each list

print('Maximum length in city1: {}'.format(max(d1.values())))
print('Minimum length in city1: {}'.format(min(d1.values())))

print('Maximum length in city2: {}'.format(max(d2.values())))
print('Minimum length in city2: {}'.format(min(d2.values())))

print('Maximum length in city3: {}'.format(max(d3.values())))
print('Minimum length in city3: {}'.format(min(d3.values())))

# c. Compare each list and determine which city is biggest & smallest with length.


print('Biggest length in city1: {}'.format(getKeysByValue(d1, max(d1.values()))))
print('Smallest length in city1: {}'.format(getKeysByValue(d1, min(d1.values()))))

print('Biggest length in city2: {}'.format(getKeysByValue(d2, max(d2.values()))))
print('Smallest length in city2: {}'.format(getKeysByValue(d2, min(d2.values()))))

print('Biggest length in city3: {}'.format(getKeysByValue(d3, max(d3.values()))))
print('Smallest length in city3: {}'.format(getKeysByValue(d3, min(d3.values()))))

# d. Delete first and last element of each list and print list contents.

city1.pop()
city1.pop(0)
print(city1)

city2.pop()
city2.pop(0)
print(city2)

city3.pop()
city3.pop(0)
print(city3)
