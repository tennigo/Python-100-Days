"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""
# 需要用到随机数,引用random模块
import random

# 定义一个answer, 先获取一个随机数
answer = random.randint(1, 100)
# 创建一个计数器, 从0开始
counter = 0

# while True表示一直执行.
while True:
    # 每轮的开始, 次数加一, 要求输入
    counter += 1
    number = int(input('请输入: '))
    # 得到输入的int后, 开始做判断
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    # 既不大也不小, 就是等于
    else:
        print('恭喜你猜对了!')
        # break终止本while循环
        break

print('你总共猜了%d次' % counter)

if counter > 7:
    print('你的智商余额明显补足')