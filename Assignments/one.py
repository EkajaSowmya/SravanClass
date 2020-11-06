def counts(lst):
    more = 0
    less = 0
    for k in range (len(lst)):
        if len(lst[k]) >= 5:
            more = more+1
        else:
            less = less+1
    return more, less
list1 = []
names = int(input("How many names u want to enter: "))
for i in range(names):
    list1.append(input())
print(list1)
more, less = counts(list1)
print("names more than 5 characters:{} " .format(more))
print(" names less than 5 characters:{}" .format(less))





