"""1.WAP to print the below asterisks pattern in increasing order
*
**
***
****
*****"""

rows = int(input("Enter the number of rows: "))
for i in range(0, rows+1):
    for j in range(i):
        print("*", end=' ')
    print(i)

"""2.WAP to print the below asterisks pattern in decreasing order using reversed built in function
*****
****
***
**
*

rows = int(input("Enter the number of rows: "))
for i in reversed(range(0, rows+1)):
    for j in range(0, i):
        print("*", end=' ')
    print()"""




