list1 = [2, 3, 'hi', 'son', 3, 3, None]#List accepts duplicate items and null values also
print(type(list1))
print(list1)
print(list1[0:3])
print(list1[0:4:3]) #here the 3rd index skip counts and prints the values between the index 0 and 4
print(list1[0:5:4]) #here the 3rd index skip counts and prints the values between the index 0 and 5
list1[3] = 'Tanav' #i am assigning the index3 element from 'son' to 'Tanav',in list we can change the item assignment
                   #we can modify the list elements which is already declared/also called mutable
print(list1)

