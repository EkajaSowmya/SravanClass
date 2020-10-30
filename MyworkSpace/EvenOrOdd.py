"""WAP to find the given number is even or odd"""
n = 8
if n % 2 == 0:
    if n >= 10:
        print(n, "is even and greater than 2")
    else:
        print(n, "is even")
else:
    print(n, "is odd")

