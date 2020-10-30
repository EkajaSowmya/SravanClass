#syntax of dictionary is dict1={keys:values}
dict1 = {3:"King", 5:"Queen", 7:"Prince", 9:200, 3:"Palace", 6:"Prince"}
#keys are always should be unique in which it will take the latest item assigned to the same keys
# whereas Values can be of duplicate
print(type(dict1))
print(dict1)
print("First name :" +dict1[3]) #3 is the key name not index
print("Second name :" +dict1[5])
print(dict1.keys())
print(dict1.values())



