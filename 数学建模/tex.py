import math as mt
import numpy as np 
xs = 0.55/(2*mt.pi)
cs = 16*mt.pi*mt.sqrt(1+(32*mt.pi)**2)+0.5*mt.log(32*mt.pi+mt.sqrt(1+(32*mt.pi)**2))
def function(theta0):
    return xs*(cs-0.5*theta0*mt.sqrt(1+theta0**2)-0.5*mt.log(theta0+mt.sqrt(theta0**2+1)))-60
a = 0
b = 100
e = 0.000000000001
c= 0
while abs(a-b)>=e:
    c = (a+b)/2
    print(c)
    if function(c)*function(a)<0:
        b = c
    else:
        a = c

print(c)

x = xs*c*mt.cos(c)
y = xs*c*mt.sin(c)
print(x,y)