import math # this function will import only to this file
x = math.sqrt(25)
print(x)
#math round up to nearest number..
# between 2.1 to 2.4 will be round upto to 2
# between 2.5 to 2.9 will be round upto to 3
print(math.floor(2.9)) #floor func will always rounds up to least value
print(math.ceil(2.2)) #ceil func will always rounds upto to highest value

print(math.pow(3, 2))
print(math.pi)
print(math.e)

#to print the value of entered expression 1+2+3-2=4
result = eval(input("enter the expression")) #using eval func
print(result)

"""command line argument not working for me
import sys
x = int(sys.argv[1])
y = int(sys.argv[2])
z = x + y
print(z)"""





