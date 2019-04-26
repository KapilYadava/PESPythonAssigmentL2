# Create 3 dictionaries (dict1, dict2, dict3) with 3 elements each. Perform following operations

dict1 = {"Name": "Kapil", "LastName": "Yadava", "Age": 30}
dict2 = {'CompanyID': 39, "Name": "Wipro", "Location": "Bangalore"}
dict3 = {'AssetID': 12, 'Name': 'Mac Laptop', 'Age': 2}

# a) Compare dictionaries to determine the biggest.
print(max(dict1.items()))
print(max(dict2.items()))
print(max(dict3.items()))
# b) Add new elements in to the dictionaries dict1, dict2
dict1['YOB'] = 1989
dict2['YOB'] = 1991
dict3['Buy'] = 2017

print(dict1)
print(dict2)
print(dict3)
# c) print the length of dict1, dict2, dict3.

print(len(dict3))
print(len(dict1))
print(len(dict2))
# d) Convert dict1, dict2, and dict3 dictionaries as string and concatenate all strings together.

dictAll = {}
dictAll.update(dict1)
dictAll.update(dict2)
dictAll.update(dict3)

print(dictAll)
