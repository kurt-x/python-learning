# 流程控制

# 逻辑操作
True and False
True or False
not False

# if else
if True:
    pass
# elif 是 else if 的缩写
elif False:
    pass
else:
    pass

# 简写
print('True') if True else print('False')

# match
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5 if day == 1:
        print('Weekday 1')
    case 1 | 2 | 3 | 4 | 5 if day == 2:
        print('Weekday 2')
    case 1 | 2 | 3 | 4 | 5:
        print('Weekday')
    case 6 | 7:
        print('Weekend')
    case _:  # 默认
        print('Unknown')

# while 循环
while True:
    if True: break
    if True: continue
else:
    print('while end')

# for 循环
for c in 'python':
    print(c, end = '')
print()

for x in range(2, 20, 3):
    print('for loop:', x)
else:
    print('for end')
