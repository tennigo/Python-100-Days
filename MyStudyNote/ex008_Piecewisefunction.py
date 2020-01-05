"""
分段函数求值
       3x - 5 (x > 1)
f(x) = x + 2 (-1 <= x <=1)
       5x + 3 (x < -1)
"""
# ex1 用了elif
# ex2 没用elif

def ex1():
    x = float(input('x = '))
    if x > 1:
        y = 3 * x - 5
    elif x >= -1:
        y = x + 2
    else:
        y = 5 * x + 3
    print('f(%.2f) = %.2f' % (x, y))

def ex2():
    x = float(input('x = '))
    if x > 1:
        y = 3 * x - 5
    else:
        if x >= -1:
            y = x + 2
        else:
            y = 5 * x + 3
    print('f(%.2f) = %.2f' % (x, y))


x = int(input('chice 1 or 2. : '))

if x == 1:
    ex1()
elif x == 2:
    ex2()
else:
    print('Error')