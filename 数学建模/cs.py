import math as mt
#原函数
#rho1 = rho0 +(0.55/(2*mt.pi))*(theta1-theta0)
#rho0**2+rho1**2-2*rho0*rho1*mt.cos(theta1-theta0)=l**2
#l_head = 1.86
#l_body = 1.65
rho0 = 8.8
theta0 = 32*mt.pi
l_head = 1.86
l_body = 1.65

def function(theta1):
    return 2*rho0**2+(0.55/mt.pi)*rho0*(theta1-theta0)+((0.55/(2*mt.pi))**2)*((theta1-theta0)**2)-2*(rho0**2)*mt.cos(theta1-theta0)-(0.55/mt.pi)*rho0*(theta1-theta0)*mt.cos(theta1-theta0)-l_head**2

