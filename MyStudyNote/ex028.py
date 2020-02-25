# 在参数名前面的*表示args是一个可变参数
def add(*args):
    total = 0
    # args是一个列表, 因为项数未知, 所以用for遍历
    for val in args:
        total += val
    return total

if __name__ == '__main__':
    # 在调用add函数时可以传入0个或多个参数
    print(add())
    print(add(1))
    print(add(1, 2))
    print(add(1, 2, 3))
    print(add(1, 2, 3, 5, 7, 9))