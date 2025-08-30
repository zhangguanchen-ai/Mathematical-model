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

    def function(unsolve):
        rho2, theta2 = unsolve[0], unsolve[1]
        return [
            float(rho[i]) - rho2 + (0.55/(2*math.pi)) * (theta2 - theta0),
            float(rho[i])**2 + rho2**2 - 2 * (float(rho[i]) * rho2) * math.cos(theta2 - theta0) - l_head_light**2
        ]

    solved = opt.fsolve(lambda unsolve: function(unsolve), [0, 0])
    theta2, rho2 = solved
    x_2 = (0.55/(2*math.pi)) * rho2 * math.cos(theta2)
    y_2 = (0.55/(2*math.pi)) * rho2 * math.sin(theta2)
    k1 = (math.sin(theta0) + theta2 * math.cos(theta0)) / math.cos(theta0) - theta0 * math.sin(theta0)
    k2 = (math.sin(theta2) + theta0 * math.cos(theta2)) / math.cos(theta2) - theta2 * math.sin(theta2)
    k = (y_0 - y_2) / (x_0 - x_2)

    try:
        alpha = math.atan(abs((k1 - k) / (1 + k1 * k2)))
        beta = math.atan(abs((k2 - k) / (1 + k1 * k2)))
    except ZeroDivisionError:
        alpha = math.pi / 2
        beta = math.pi / 2

    print(f"时刻: {time}")
    print(f"rho[i]: {float(rho[i])}")
    print(f"theta0: {float(theta0)}")
    print(f"theta2: {float(theta2)}")
    print(f"rho2: {float(rho2)}")
    print(f"x_2: {float(x_2)}")
    print(f"y_2: {float(y_2)}")
    print(f"alpha: {float(alpha)}")
    print(f"beta: {float(beta)}")

    # 新增代码：计算指定节数的变化
    x_prev = x_2
    y_prev = y_2
    theta_prev = theta2
    rho_prev = rho2
    target_data = {}

    for section in range(1, l_totality_joint + 1):
        def section_function(unsolve):
            rho_current, theta_current = unsolve[0], unsolve[1]
            return [
                float(rho_prev) - rho_current + (0.55/(2*math.pi)) * (theta_current - theta_prev),
                float(rho_prev)**2 + rho_current**2 - 2 * (float(rho_prev) * rho_current) * math.cos(theta_current - theta_prev) - l_light_body_joint**2
            ]

        solved = opt.fsolve(lambda unsolve: section_function(unsolve), [rho_prev, theta_prev])
        theta_current, rho_current = solved
        x_current = (0.55/(2*math.pi)) * rho_current * math.cos(theta_current)*10
        y_current = (0.55/(2*math.pi)) * rho_current * math.sin(theta_current)*10

        if section in target_sections:
            target_data[section] = {
                'x': x_current,
                'y': y_current,
                'rho': rho_current,
                'theta': theta_current
            }

        x_prev = x_current
        y_prev = y_current
        theta_prev = theta_current
        rho_prev = rho_current

    for section in target_sections:
        data = target_data[section]
        print(f"第 {section} 节:")
        print(f"  x: {data['y']}")
        print(f"  y: {data['x']}")
        print(f"  rho: {data['rho']}")
        print(f"  theta: {data['theta']}")

    print("-" * 30)