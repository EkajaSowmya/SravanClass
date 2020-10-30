"""WAP to print the pattern
1234
234
34
4
"""
for i in range(5):
    for j in range(i+1,5):
        print(j,end=" ")
    print()
