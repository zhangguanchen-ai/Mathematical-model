import math as mt
import scipy.optimize as opt
import numpy as np 

t = [60, 120, 180, 240, 300]
d = 0.55
v0 = 1.0
total_time = 300
num_point = 223
l_head_light = 2.86
xs = 0.55/(2*mt.pi)
cs = 16*mt.pi*mt.sqrt(1+(32*mt.pi)**2)+0.5*mt.log(32*mt.pi+mt.sqrt(1+(32*mt.pi)**2))

# 定义计算 theta0 的函数，传入 theta0 和具体的时间 time
def calculate_theta0(theta0, time):
    return xs*(cs - 0.5*theta0*mt.sqrt(1 + theta0**2) - 0.5*mt.log(theta0 + mt.sqrt(theta0**2 + 1))) - time

# 二分查找函数
def binary_search(time, a=0, b=100, e=0.0000001):
    c = 0
    while abs(a - b) >= e:
        c = (a + b) / 2
        if calculate_theta0(c, time) * calculate_theta0(a, time) < 0:
            b = c
        else:
            a = c
    return c

# 定义计算 rho2 和 theta2 的函数
def calculate_rho_theta(unsolve):
    rho2, theta2 = unsolve
    return [
        rho1 - rho2 + (0.55/(2*mt.pi)) * (theta2 - theta0),
        rho1**2 + rho2**2 - 2 * rho1 * rho2 * mt.cos(theta2 - theta0) - l_head_light**2
    ]

for time in t:
    # 使用二分查找计算 c
    c = binary_search(time)
    x_0 = xs * c * mt.cos(c)
    y_0 = xs * c * mt.sin(c)
    rho1 = mt.sqrt(x_0**2 + y_0**2)
    theta0 = c

    # 求解 rho2 和 theta2
    solved = opt.fsolve(lambda unsolve: calculate_rho_theta(unsolve, rho1, theta0), [0, 0])
    theta2, rho2 = solved
    x_2 = rho2 * mt.cos(theta2)
    y_2 = rho2 * mt.sin(theta2)

    print(f"时刻 {time} 的龙头数据:")
    print(f"c: {c}")
    print(f"x龙头: {x_0}")
    print(f"y龙头: {y_0}")
    print("-" * 20)
    print(f"rho1: {rho1}")
    print(f"theta1: {theta0}")
    print(f"rho2: {rho2}")
    print(f"theta2: {theta2}")
    print(f"x2: {x_2}")
    print(f"y2: {y_2}")
    print("=" * 20)

'''
#龙头数据
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
'''