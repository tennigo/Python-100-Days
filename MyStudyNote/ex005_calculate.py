# 用到math.pi
import math

# 要求用户输入一个数字作为圆的半径,
# 转换为float.
radius = float(input('请输入圆的半径: '))
# 根据公式计算周长和面积
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius

# 输出结果,用了精度2个小数点的占位符.
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)
