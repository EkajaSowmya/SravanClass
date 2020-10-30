"""1.WAP to print the below asterisks patern in decreasing order
*****
****
***
**
*
"""
rows = int(input("Enter the number of rows: "))
for i in range(rows, 0, -1):
    for j in range(0, i):
        print("*", end=' ')
    print()

"""2.WAP to print the sum of two numbers with user inputs.
x = int(input("enter the first number"))#if u don't specify int here, by default it 
                                        #will consider the input as string and prints the 
                                        #output as string itself.  
                                        
y = int(input("enter the second number"))
z = x + y
print(z)"""

