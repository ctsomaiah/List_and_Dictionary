# Common topics:
# https://www.techbeamers.com/python-programming-questions-list-tuple-dictionary/
# https://www.datacamp.com/community/tutorials/18-most-common-python-list-questions-learn-python
#
# List:
# https://www.w3resource.com/python-exercises/list/
# https://www.geeksforgeeks.org/python-list/
# 1
print("1. Create an empty list and append values using iteration")
l = []
for i in range(2, 15, 2):
    a = l.append(i)
print(l)

# 2
print("\n2. Create a list and access elements in it")
l = [[2, 4, 6, 8, 10, 12, 14]]
for i in l:
    print(i, end=" ")

# 3
print("\n\n3. Create a list and remove elements from a list")
l = [2, 4, 6, 8, 10, 12, 14]
l.remove(8)
print(l)

# 4
print("\n4. Create a list and slice elements in it")
Lst = [50, 70, 30, 20, 90, 10, 50]
print(Lst[::])

# 5
print("\n5. Write a Python program to sum all the items in a list using the function")
Lst = [50, 70, 30, 20, 90, 10, 50]
print(Lst[::])

# 6
print("\n6. Write a Python program to multiply all the items in a list using the function")


# Python program to multiply all values in the
# list using traversal
def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result


list1 = [3, 2, 4]
print(multiplyList(list1))

# 7
print("\n7. Get the largest number from a list using the function")
list1 = [3, 2, 4, 8, 7, 5]
print(list1)
print("Highest value is :", max(list1))

# 8
print("\n8. Remove duplicates from a list")
l = [1, 2, 4, 2, 1, 4, 5]
print("Original List: ", l)
res = [*set(l)]
print("List after removing duplicate elements: ", res)

# 9
print("\n9. Check whether a list is empty or not")
l = [1, 2, 4, 2, 1, 4, 5]
if len(l) == 0:
    print("List is empty")
else:
    print("List is not empty")

# 10
print("\n10. Get the frequency of the elements in a list")
# a = [1,1,2,2,2,3,3,3,3,4,4,4,4,4]
# Expected output: {1:2,2:3,3:4,4:5}
a = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4]
d = {x:a.count(x) for x in a}
print(d)

# 11
print("\n11. Count the number of elements in a list within a specified range")
l = [9, 20, 88, 452, 78, 152, 413, 425]
print(l)
s = sum(1 < x < 100 for x in l)
print(s)

# 12. Difference between the two lists
#
print("\n<----------------------------------------------------------------------------------------------------->\n")
# Dictionary:
# https://www.geeksforgeeks.org/python-dictionary/
# https://www.w3resource.com/python-exercises/dictionary/
# 1
print("1. Create a nested dictionary")
Dict = {1: 'Geeks', 2: 'For', 3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}
print(Dict)

# 2
print("\n2. Create a dict, add elements to it, add a set of values to a key")
dict1 = {}
dict1['key1'] = 'Hello'
dict1['key2'] = 'World'
print("Dict contains:", dict1)

# 3
print("\n3. Update existing Key's Value, Add Nested Key value to Dictionary")
dict1 = {'key1': 'geeks', 'key2': 'fill_me'}
print("Current Dict is: ", dict1)
dict1['key2'] = 'for'
dict1['key3'] = {'key4': 'Hello', 'key5': 'World'}
print("Updated Dict is:", dict1)

# 4
print("\n4. Create a dict with keys and values, access key 1, and access using the GET function")
dict1 = {'key1': 'val1', 'key2': 'val2', 'key3': 'val3', 'key4': 'val4'}
print(dict1.get('key1'))
print(dict1.get('key4'))

# 5
print("\n5. Create a nested dict with keys and values, delete key 2")
Dict = {1: 'Geeks', 2: 'For', 3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}
print('Before deleting -', Dict)
del Dict[2]
print('After deleting -', Dict)

# 6
print("\n6. Delete a key from a nested dict, use the POP function, and delete entire dict")
dict1 = {'key1': 'val1', 'key2': 'val2', 'key3': 'val3', 'key4': 'val4'}
print("Before pop", dict1)
dict1.popitem()
dict1.pop('key2')
print("After pop :", dict1)

# 7
print("\n7. Check whether a dictionary is empty or not")
test_dict = {}
print("The original dictionary : " + str(test_dict))
res = len(test_dict) == 0
print("Is dictionary empty ? : " + str(res))

# 8
print("\n8. Add a key to a dictionary")
dict1 = {'key1': 'geeks', 'key2': 'fill_me'}
print("Current Dict is:", dict1)
dict1['key2'] = 'for'
dict1['key3'] = 'geeks'
print("Updated Dict is:", dict1)

# 9
print("\n9. Check if a given key already exists in a dictionary")
dict1 = {'key1': 'val1', 'key2': 'val2', 'key3': 'val3', 'key4': 'val4'}
res = 'key2'
if res in dict1.keys():
    print(res, "exists")
else:
    print(res, "doesn't exist")

# 10
print("\n10. Iterate over dictionaries using for loops")
dict1 = {'key1': 'val1', 'key2': 'val2', 'key3': 'val3', 'key4': 'val4'}
for key in dict1:
    print(key, 'corresponds to', dict1[key])

# 11
print("\n11. Sum all the items in a dictionary")
d = {'key1': 1, 'key2': 14, 'key3': 47}
print(sum(d.values()))

# 12
print("\n12. Multiply all the items in a dictionary")
d = {'value1': 5, 'value2': 4, 'value3': 3, 'value4': 2, 'value5': 1}
print("Dict is :", d)
answer = 1
for i in d:
    answer = answer * d[i]
print(answer)

#13
print("\n13. Remove a key from a dictionary")
d = {'value1': 5, 'value2': 4, 'value3': 3, 'value4': 2, 'value5': 1}
print("Before :",d)
d.popitem()
print("After :",d)

#14
print("\n14. Get the maximum and minimum value in a dictionary")
d = {'a':11, 'b':12, 'c':18, 'd':15}
print(d)
res = min(d)
res1 = max(d)
print("Min is:",res,":",d[res])
print("Max is:",res1,":",d[res1])

#15
print("\n15. Find the highest 3 values in a dictionary")
from collections import Counter
my_dict = {'A': 67, 'B': 23, 'C': 45, 'D': 56, 'E': 12, 'F': 69}
k = Counter(my_dict)
high = k.most_common(3)
print("Initial Dictionary:")
print("Dictionary with 3 highest values:")
print("Keys: Values")
for i in high:
	print(i[0]," :",i[1])

#16
print("\n16. Sort a list alphabetically in a dictionary")
num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
print("Before sorting :",num)
sorted_dict = {x: sorted(y) for x, y in num.items()}
print("After sorting :",sorted_dict)

#
# Tuple:
# https://www.geeksforgeeks.org/tuples-in-python/
# https://www.w3resource.com/python-exercises/tuple/
