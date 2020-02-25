from random import randint

def roll_dice(n=2):
    """摇骰子"""
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total

def add(a=0, b=0, c=0):
    """三个数相加"""
    return a + b + c

if __name__ == '__main__':
    # 如果没有指定参数, 使用默认值
    print(roll_dice())
    # 指定参数, 按参数执行
    print(roll_dice(3))

    # 使用默认参数
    print(add())
    # 给第一个参数
    print(add(1))
    # 给第一个, 第二个参数
    print(add(1, 2))
    # 给三个参数
    print(add(1, 2, 3))
    # 不按顺序指定参数
    print(add(c=50, a=100, b=200))