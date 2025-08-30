import math as mt
import scipy.optimize as opt
import numpy as np 

t = [0, 60, 120, 180, 240, 300]
d = 0.55
v0 = 1.0
total_time = 300
num_point = 223
l_head_light = 2.86
xs = 0.55/(2*mt.pi)
cs = 16*mt.pi*mt.sqrt(1+(32*mt.pi)**2)+0.5*mt.log(32*mt.pi+mt.sqrt(1+(32*mt.pi)**2))
j=0
l_light_body_light = 1.65
l_light_body_joint = [1,60,120,180,240,300]
l_light_tail = 1.65
def function(x):
    return xs*(cs - 0.5*x*mt.sqrt(x**2+1)-0.5*mt.log(x+mt.sqrt(x**2+1)))
# 定义计算 theta0 的函数，传入 theta0 和具体的时间 time
def calculate_theta0(theta0, time):
    return xs*(cs - 0.5*theta0*mt.sqrt(1 + theta0**2) - 0.5*mt.log(theta0 + mt.sqrt(theta0**2 + 1))) - time

# 二分查找函数
def binary_search(time, a, b, e=0.00000001):
    c = 0
    while abs(a - b) >= e:
        c = (a + b) / 2
        if calculate_theta0(c, time) * calculate_theta0(a, time) < 0:
            b = c
        else:
            a = c
    return c
def search(fun, a, b, e=0.00000001):
    c = 0
    while abs(a - b) >= e:
        c = (a + b) / 2
        if fun(c)*fun(a) < 0:
            b = c
        else:
            a = c
    return c

j = 0
u=[0,0,0,0,0,0]
kfc = [0,0,0,0,0,0]
for time in t:

    # 使用二分查找计算 c
    c = binary_search(time,0,100)
    x_0 = xs * c * mt.cos(c)
    y_0 = xs * c * mt.sin(c)
    rho1 = (0.55/(2*mt.pi))*c

    print(c,x_0,y_0,rho1)
    u[j]=c
    kfc[j]=rho1
    j=j+1
i = 0
def function(theta2):
    return 2*kfc[i]**2+(0.55/mt.pi)*(theta2-u[i])+((0.55/(2*mt.pi))**2)*(theta2-u[i]**2)-2*kfc[i]**2*mt.cos(theta2-u[i])+(0.55/mt.pi)*kfc[i]*(theta2-u[i])*mt.cos((theta2-u[i]))-2.86**2
s_1 = 100.5
s_2 = 105
while i<=5:

    x = search(function,s_1,s_2)
    print(x)
    s_1 = s_1-10
    s_2 = s_2-10
    x_2 = xs * x * mt.cos(x)
    y = xs * x * mt.sin(x)
    print(x_2)
    print(y)
    i+=1