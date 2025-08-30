import math as mt
import xlrd as xl
xs = 0.55/(2*mt.pi)
cs = 16*mt.pi*mt.sqrt((32*mt.pi)**2+1)+0.5*mt.log(32*mt.pi+mt.sqrt((32*mt.pi)**2+1))

def function(x):
    return xs*(cs - 0.5*x*mt.sqrt(x**2+1)-0.5*mt.log(x+mt.sqrt(x**2+1)))


d=0
a=0.0000000001
b=-100
c=110
for i in range(0,301,60):
    while abs(b-c)>=a:
        d = (b+c)/2
        if (function(b)-i)*(function(d)-i)<0:
            c = d
        else:
            b = d
    x_0 = xs * d * mt.cos(d)
    y_0 = xs * d * mt.sin(d)
    theta = xs*d
    print(x_0,y_0,d)
    d=0
    a=0.0000000001
    b=-100
    c=110



