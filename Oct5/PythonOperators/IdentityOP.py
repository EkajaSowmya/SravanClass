a = 3
b = 4
print("integers-", a is b, a is not b)

x1 = "PYTHON"
x2 = "python"
print("string-", x1 is x2, x1 is not x2)

l1 = [1,2,3]
l2 = [1,2,3]
print("list-", l1 is l2, l1 is not l2)

t1 = (4,5,6)
t2 = (4,5,6)
print("tuple-", t1 is t2, t1 is not t2)

d1 = {1:"apple", 2:"grapes", 3:12}
d2 = {1:"apple", 2:"grapes", 3:12}
print("dict-", d1 is d2, d1 is not d2)

b1 = True
b2 = False
print("bool-", b1 is b2, b1 is not b2)

s1 = (7,8,9)
s2 = (7,8,9)
print("set-",s1 is s2, s1 is not s2)
