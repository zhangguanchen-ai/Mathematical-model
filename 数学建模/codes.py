import math as mt
import scipy as sc
import numpy as np
i = 1
t = [0,60,120,180,240,300]
def helix_length_dragonhead(theta0):
    return (0.55/(2*mt.pi))*(16*mt.pi*mt.sqrt(1+32*32*mt.pi*mt.pi)+0.5*mt.log(32*mt.pi+mt.sqrt(1+32*32*mt.pi*mt.pi))-0.5*theta0*mt.sqrt(1+theta0**2)+0.5*mt.log(theta0+mt.sqrt(1+theta0**2)))-t[i]

while(i<6):
    s = sc.optimize.fsolve(helix_length_dragonhead,1)
    x_0 = (0.55/(2*mt.pi))*s*mt.cos(s)
    y_0 = (0.55/(2*mt.pi))*s*mt.sin(s)
    print(x_0,y_0)
    i+=1
