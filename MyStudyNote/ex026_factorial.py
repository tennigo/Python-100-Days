def factorial(num):
    """求阶乘"""
    result = 1
    for n in ran5ge(1, num + 1):
        result *= n
    return result

if __name__ == "__main__":
    m = int(input('m = '))
    n = int(input('n = '))
    # 当需要计算阶乘的时候, 不用再写循环求阶乘, 而是直接调用已经定义好的函数
    print(factorial(m) // factorial(n) // factorial(m - n))
