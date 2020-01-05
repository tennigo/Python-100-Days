"""
判断输入的边长能否构成三角形,
如果能则计算出三角形的周长和面积.
"""

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a + b > c and a + c > b and b + c > a:
    print('周长: %.2f' % (a + b + c))
    p = (a + b + c) / 2
    # 面积用的是海伦公式
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('面积: %.2f' % (area))
else:
    print('不能构成三角形')