n = int(input('Enter n: '))
sign = 0
if n < 0:
   sign = -1
   n = (-n)
else:
   sign = 1
f = 1
m = 1
while m <= n:
   f= f * m
   m += 1
print(f * sign)