# Create a list with 7 elements and perform following operations.
# Let the list be initialized with List1 any 5 city names;

city1 = ["Delhi", "Mumbai", "Kolkata", "Chennai", 'Bangalore']

# a) Append a new city name to the List
city1.append('Gurgaon')
print(city1)
# b) Insert a city name at 4th index position
city1.insert(4, 'Noida')
print(city1)
# c) Sort the list and print all elements
print(sorted(city1))
# d) Sort the elements of the list in descending order.
print(sorted(city1, reverse=True))
# e) delete last three elements using pop operation
city1.pop()
city1.pop()
city1.pop()
print(city1)
