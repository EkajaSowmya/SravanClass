""" print the pattern below
APQR
ABQR
ABCR
ABCD"""

x='ABCD'
y='PQR'
for i in range(4):
      print(x[:i+1]+y[i:])
