"""1.WAP to check the given number is positive or negative using elif
n = -3
if n > 0:
    print("Number is positive", n)
elif n == 0:
    print("Number is Zero", n)
else:
    print("Number is negative", n)
"""

"""1.WAP to check the given number is positive or negative using nested if"""
n = 4
if n >= 0:
    if n == 0:
        print(n, "Number is equal to zero")
    else:
        print(n, "Number is Positive")
else:
    print(n, "is Negative number")
