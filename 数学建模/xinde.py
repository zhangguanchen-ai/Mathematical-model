import math as mt
import scipy as sc
rho0 = 8.8
theta0 = 32*mt.pi
l_head = 2.86
l_body = 1.65
j = 0
qs = 101
while j<=222:
    def function(theta1):
        return 2*rho0**2+(0.55/mt.pi)*rho0*(theta1-theta0)+((0.55/(2*mt.pi))**2)*((theta1-theta0)**2)-2*(rho0**2)*mt.cos(theta1-theta0)-(0.55/mt.pi)*rho0*(theta1-theta0)*mt.cos(theta1-theta0)-l_head**2 
    sol = sc.optimize.fsolve(function,qs)
    qs+=1
    print(sol)
    j+=1
    l_head = l_body
    
    theta0 = sol[0]
    rho0 = (0.55/(2*mt.pi))*theta0
    print(rho0)
