import math as mt
rho0 = 8.8
theta0 = 32*mt.pi
l_head = 2.86
l_body = 1.65
def function(theta1):
    return 2*rho0**2+(0.55/mt.pi)*rho0*(theta1-theta0)+((0.55/(2*mt.pi))**2)*((theta1-theta0)**2)-2*(rho0**2)*mt.cos(theta1-theta0)-(0.55/mt.pi)*rho0*(theta1-theta0)*mt.cos(theta1-theta0)-l_head**2 
def function_1(theta1):
    return (0.55/mt.pi)*rho0+2*rho0**2*mt.sin(theta1-theta0)-(0.55/mt.pi)*rho0*mt.cos(theta1-theta0)+(0.55/mt.pi)*rho0*(theta1-theta0)*mt.sin(theta1-theta0)
i = 0
j = 0
x_0 = 101
x_n = 0
while j<=222:
    while i<=12:
        x_n =  x_0 - (function(x_0)/function_1(x_0))
        i = i+1
        x_0=x_n
    m_1 = (0.55/(2*mt.pi))*x_0*mt.cos(x_0)
    m_2 = (0.55/(2*mt.pi))*x_0*mt.sin(x_0)
    m_3 = (0.55/(2*mt.pi))*x_0
    print(m_1,m_2,m_3)
    j = j+1
    l_head = l_body
    rho0 = m_3
    theta0 = x_n
    x_0 = 101
    x_n = 0
    i = 0
