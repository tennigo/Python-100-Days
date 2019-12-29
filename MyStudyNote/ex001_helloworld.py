"""
第一个Python程序 - hello, world!
向伟大的Dennis M. Ritchie先生致敬

Version: 0.1
Author: 骆昊
"""

# *英文可以
print('hello, world!')

# *下面一行, 演示注释符号'#'的用法
# print("你好,世界!")

# *中文亦无问题
# *中间用逗号,可以串联多个字符串,输出结果默认用空格连接
print('你好', '世界')

# *sep=', ', 意思是字符串之间用', '连接. 默认是一个空格
# *end='!', 意思是结尾用'!'(不换行), 默认是换行(就是\n)
print('hello', 'world', sep=', ', end='!')
print('goodbye, world', end='!\n')