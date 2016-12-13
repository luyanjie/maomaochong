import math


def quadratic(a,b,c):
    if not isinstance(a,(int,float)) and isinstance(b,(int,float)) and isinstance(c,(int,float)):
        raise TypeError('bad operand type')
    if a == 0:
        return 'a不能为0'
    n = float(b * b - 4 * a * c)
    if n < 0:
        return '方程无解'
    elif n == 0:
        x = int(-b/(2*a))
        return '方程的解为：x=%.1f'% x

    else:
        x1 = (-b + math.sqrt(n))/(2*a)
        x2 = (-b - math.sqrt(n))/(2*a)
        return '方程的解为：x1=%.1f,x2=%.1f'%(x1,x2)

print(quadratic(1,1,1))



def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

n = my_abs(-20)
print(n)

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

# TypeError: bad operand type:
#my_abs('123')