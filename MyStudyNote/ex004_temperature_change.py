# ask user input a float type number.
f = float(input('请输入华氏温度: '))
# change f to c use formula.
c = (f - 32) / 1.8
# print the result100
print('%.1f华氏度 = %.1f摄氏度' % (f, c))
