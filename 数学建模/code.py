import numpy as np
import scipy as sc
import math as mt
d = 0.55
v = 1
t = [0,60,120,180,240,300]
l_head = 286
l_body = 165
def function_helix(a,theta):
    return (a/(2*mt.pi))*theta

def helix_length_dragonhead(theta0):
    return 16*mt.pi*mt.sqrt(1+32*32*mt.pi*mt.pi)+0.5*mt.log(32*mt.pi+mt.sqrt(1+32*32*mt.pi*mt.pi))-theta0*0.5*mt.sqrt(1+theta0*theta0)-0.5*mt.log(theta0+sqrt(1+theta0*theta0))