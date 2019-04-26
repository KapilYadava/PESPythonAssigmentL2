# Create 2 dictionaries as follows;
# dict1 ={'Name':'Ramakrishna','Age':25}
# dict2={'EmpId':1234,'Salary':5000}

dict1 = {'Name': 'Ramakrishna', 'Age': 25}
dict2 = {'EmpId': 1234, 'Salary': 5000}

# Perform following operations
# a) Create single dictionary by merging dict1 and dict2

dict1 = {'Name': 'Ramakrishna', 'Age': 25}
dict2 = {'EmpId': 1234, 'Salary': 5000}

dictAll = {}
dictAll.update(dict1)
dictAll.update(dict2)

print(dictAll)

# b) Update the salary to 10%
dictAll.update({'Salary': '10%'})
print(dictAll)
# c) Update the age to 26
dictAll.update(({'Age': 26}))
print(dictAll)
# d) Insert the new element with key "grade" and assign value as "B1"
dictAll['grade'] = 'B1'
print(dictAll)
# e) Extract and print all values and keys separately.
for key, item in dictAll.keys() and dictAll.items():
    print(key, item)
# f) delete the element with key 'Age' and print dictionary elements.
dictAll.pop('Age')
print(dictAll)
