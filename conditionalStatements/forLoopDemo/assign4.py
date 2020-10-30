"""1.WAP to print the intergers and strings in separate lines from the given list
integers printed separately [4, 6, 7, 2, 1]


strings printed separately ['hello', 'hi', 'table', 'sun']
-----------------------------------------------------------"""

list1 = [4, 6, 'hello', 'hi', 'table',7, 2, 1,'sun']
integer_list = []
string1_list = []
for each_item in list1:
    if isinstance(each_item, int):
        integer_list.append(each_item)
    else:
        string1_list.append(each_item)

print("integers printed separately",integer_list)
print("\n\nstrings printed separately", string1_list)

"""2.WAP to print the below output
each integer item = 4
each integer item = 6
each string item = hello
each string item = hi
each string item = table
each integer item = 7
each integer item = 2
each integer item = 1
each string item = sun
integers printed separately [4, 6, 7, 2, 1]


strings printed separately ['hello', 'hi', 'table', 'sun']
--------------------------------------------------------------

list1 = [4, 6, 'hello', 'hi', 'table',7, 2, 1,'sun']
integer_list = []
string1_list = []
for each_item in list1:
    type_of_each_item = type(each_item)
    if type_of_each_item == int:
        print("each integer item =", each_item)
        integer_list.append(each_item)
    else:
        print("each string item =", each_item)
        string1_list.append(each_item)

print("integers printed separately",integer_list)
print("\n\nstrings printed separately", string1_list)"""

