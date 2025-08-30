import math
import scipy.optimize as opt

t = [0, 60, 120, 180, 240, 300]
l_totality_joint = 223
l_head_light = 2.86
l_light_body_light = 1.65
l_light_body_joint = 2.21
l_light_tail = 1.65

rho = [0] * 6
# 修改函数，传入 time 参数
def helix_length_dragonhead(theta0, time):
    return (0.55/(2*math.pi))*(16*math.pi*math.sqrt(1+32*32*math.pi*math.pi)+0.5*math.log(32*math.pi+math.sqrt(1+32*32*math.pi*math.pi))-0.5*theta0*math.sqrt(1+theta0**2)+0.5*math.log(theta0+math.sqrt(1+theta0**2)))-time

target_sections = [51, 101, 151, 201]

for i, time in enumerate(t):
    s = opt.fsolve(lambda theta0: helix_length_dragonhead(theta0, time), 1)
    theta0 = float(s)
    rho[i] = (0.55/(2*math.pi)) * s
    x_0 = (0.55/(2*math.pi)) * s * math.cos(s)
    y_0 = (0.55/(2*math.pi)) * s * math.sin(s)
    rho1 = math.sqrt(x_0**2 + y_0**2)
    print(rho[i])
    print(x_0)
    print(y_0)
    print(rho1)