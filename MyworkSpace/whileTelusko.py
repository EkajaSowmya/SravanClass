"""WAP to print all the values from 1 to 100. Skip the nos which are
divisible by 3 or 5"""

i = 1
while i <= 100:
    if i%3!=0 and i%5!=0:
        print(i, end=" ")
    i = i + 1
print()

"""WAP to 5 skip count in 100 
for i in range(1, 100, 5):
    print(i, end=" ")
"""




