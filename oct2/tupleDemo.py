tuple1 = (2, 3, 'hi', 'son', 3, 3, None)#tuple also accepts duplicate items and null values
print(type(tuple1))
print(tuple1)
print(tuple1[0:3])
print(tuple1[0:4:3]) #here the 3rd index skip counts and prints the values between the index 0 and 4
print(tuple1[0:5:4]) #here the 3rd index skip counts and prints the values between the index 0 and 5
tuple1[3] = 'Tanav' #i am assigning the index3 element from 'son' to 'Tanav'.
                    # In tuple we can't change the item assignment/also called immutable
                    #we can't modify the tuple elements which is already declared once
print(tuple1)