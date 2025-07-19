# 数据
from types import NoneType

v = 1  # 声明变量
v = '123'  # 再次声明覆盖之前的同名变量
x, y, z = 1, 2, 3  # 同时赋值多个变量
x = y = z = '123'

# 拆包
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

int(3)  # 3
str(3)  # '3'
float(3)  # 3.0

g = 1


def fun():
    global g  # 声明一个全局作用域的变量
    g = 10


fun()

print('global g:', g)

# 数据类型
print('type of v:', type(v))  # 获取数据类型

str  # 文本类型
print('type of "123"', type('123'))

int, float, complex  # 数值类型
print('int:', type(1), type(0b1), type(0o1), type(0x1))
print('float:', type(1.0), type(1e2))
print('type of 1j:', type(1j))

list, tuple, range  # 序列类型
dict  # 映射类型
set, frozenset  # 集合类型
bool  # 布尔类型
bytes, bytearray, memoryview  # 二进制类型
NoneType  # None 类型

# 字符串
hello = 'Hello, world!'
print('index 0:', hello[0])
print('len:', len(hello))
print('check in:', 'Hel' in hello)
print('check not in:', 'hel' not in hello)
print('slice of string:', hello[2:6], hello[6:], hello[:5], hello[-5:-2])
print('upper:', hello.upper())
print('lower:', hello.lower())
h = '  Hello, world!  '
print('strip:', h.strip())
a = 'Hello,'
b = 'world!'
print('concat:', a + ' ' + b)
pi = 3.1415926
print('format:', f'{'p' + 'i'} = {pi:.2f}')
