#project 1 - evaluate pi to nth digit
import math
from decimal import *
getcontext()
N = raw_input("Enter the digit till which you want the pi to be evaluated: ")
getcontext().prec = int(N)+1
i=Decimal('0.0')

n=0
z=Decimal('0.0')
den=Decimal('0.0')
y=z
size=0
# using Leibniz formula for evaluating pi as the standard constant in python only prints 3.14159265359

#N=10
#while size < int(N):
while n<1000000:
    i = math.pow(-1,n)
    den = 2*n+1
    y = i/den
    z = z+Decimal(y)
    pi_chunk = 4*z
    size = len(str(pi_chunk))
    n=n+1
print (pi_chunk)  
 
