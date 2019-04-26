# Create two tuples tup1 & tup2 and apply all built in functions on tuples.
# ( Refer Tutorial for the Built in functions list)

tup1 = (8, 2, 4, 9, 7)
tup2 = (0, -2, 6, 15, 8, 4, 9, 4, 4)

print(tup1 + tup2)
print(tup2.count(4))
print(tup2.__eq__(tup1))
print(tup1.__contains__(-3))

for item in tup1.__iter__():
    print(item)
print(tup1.__add__(tup2))
print(tup2.__len__())
