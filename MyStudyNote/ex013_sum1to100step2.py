sum = 0

for x in range(2, 101, 2):
    sum += x

print(sum)

# 方法2

sum2 = 0

for x in range(1, 101):
    if x % 2 == 0:
        
        sum2 += x

print(sum2)