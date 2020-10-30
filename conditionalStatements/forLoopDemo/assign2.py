"""1.WAP to print the below patern
- 1 - 3 - 5
- 1 - 3 -
- 1 - 3
- 1 -
-
"""

rows = int(input("Enter the number of rows: "))
for i in reversed(range(0, rows+1)):
    for j in range(0, i+1):
        if j%2 == 0:
            print("-", end=' ')
        else:
            print(j, end=' ')
    print()