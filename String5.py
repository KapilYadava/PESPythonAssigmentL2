# Create Tuple as specified below;
# a) Create a Tuple tup1 with days in a week & print the tuple elements

tup1 = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
for day in tup1:
    print(day, end=' ')

# b) Create a Tuple tup2  with months in a year and concatenate it with tup1
print()
print('#' * 100)
tup2 = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
        'August', 'September', 'October', 'November', 'December')
for month in tup2:
    print(month, end=' ')
print()
for month in tup2 + tup1:
    print(month, end=' ')

# c) Create 3 tuples( tup1,tup2,tup3) with numbers and determine which is greater.
print()
tup1 = (1, 2, 6, 5)
tup2 = (8, 2, 4, 9, 7)
tup3 = (0, -2, 6, 15, 8, 4, 9)

print(max(tup1))
print(max(tup2))
print(max(tup3))
# d) Try to delete an individual element in tup1 and try deleting complete Tuple -tup1 notice the error type you get.
print()
l = list(tup1)
l.pop()
l.pop()
# l.pop()
# l.pop()
# l.pop()
tup1 = tuple(l)
print(tup1)

# e) Insert new element in to tuple by typecasting it to List

l2 = list(tup2)
l2.append(10)
l2.append(55)
tup2 = tuple(l2)
print(tup2)
