
def zero(fuc,a,b,c):
    while abs(b-c)>=a:
        d = (b+c)/2
        if fuc(b)*fuc(d)<0:
            b = d
        else:
            c = d
    return (b+c)/2