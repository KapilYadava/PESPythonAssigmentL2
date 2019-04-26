# Create 3 Lists (list1, list2, list3) with integer and perform following operations

list1 = [1, 2, 4, 4, 6]
list2 = [4, 7, 9, 55, 6]
list3 = [3, 8, 2, 1, 85]
maxlist = list()
minlist = list()
# a) Create Maxlist by taking 2 maximum elements from each list.

for l in [list1, list2, list3]:
    biggest = max(l)
    l.remove(biggest)
    second_biggest = max(l)
    maxlist.append(biggest)
    maxlist.append(second_biggest)

print('MaxList: {}'.format(maxlist))

# b) Find average value from all the elements of Maxlist.
print('Average of maxlist: {}'.format(sum(maxlist) / len(maxlist)))
# c) Create a MinlIst by taking 2 minimum elements from each list

for l in [list1, list2, list3]:
    biggest = max(l)
    l.remove(biggest)
    second_biggest = max(l)
    minlist.append(biggest)
    minlist.append(second_biggest)
print('MinList: {}'.format(minlist))

# d) Find the average value from all the elements of Minlist

print('Average of minlist: {}'.format(sum(minlist) / len(minlist)))
