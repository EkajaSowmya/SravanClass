"""1.WAP to print the following pattern below by skipping even number rows
* * * * *

* * *

*

"""

rows = int(input("Enter the number of rows: "))
for i in reversed(range(0, rows+1)):
    for j in range(0, i+1):
        if i % 2 == 0:
            print("*", end=' ')
        else:
            print(end=' ')
    print()