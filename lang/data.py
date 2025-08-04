# 数据
from types import NoneType

v = 1  # 声明变量
v = '123'  # 再次声明覆盖之前的同名变量
x, y, z = 1, 2, 3  # 同时赋值多个变量
x = y = z = '123'
del x  # 删除变量
# print(x)  # 报错

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
    f = 10

    def inner_fun():
        nonlocal f
        f = 5

    inner_fun()
    print('nonlocal data:', f)

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

# 字符串（字符数组）
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

# 布尔值
print('boolean:', True, False)
print('None 是 False:', bool(None))
print('除空字符串外的所有字符串都可以作为 True:', bool('123'), bool(''))
print('除 0 外的所有数字都可以作为 True:', bool(1), bool(-1), bool(0))
print('任何非空的 list,tuple,set,dict 都可以作为 True:', bool([1]))

'''
集合（数组） collections(arrays)
  - list(列表)   有序、可变、允许重复
  - tuple(元组)  有序、不可变、允许重复
  - set(集合)    无序、不可变、没有重复、无索引
  - dict(字典)   有序、可变、没有重复
'''

collection = [1, 2, 3, 4, 5]
# 遍历集合
for item in collection: pass
for item in range(len(collection)): pass
# 集合计算
print('collection compute', [1, 2] + [3, 4])  # 合并集合
print('collection compute', [1, 2] * 2)  # 重复集合
# 索引
print('negative indexing:', collection[-1])  # 负索引，指向倒数第一个元素
print('range of indexes[2:4]:', collection[2:4])  # 指向索引 2(include)-4(not include) 之间的元素
print('range of indexes[2:]:', collection[2:])  # 指向索引 2(include) 之后的所有元素
print('range of indexes[:4]:', collection[:4])  # 指向索引 4(not include) 之前的所有元素
# 检查是否存在
print('check existence:', 1 in [1, 2])  # 检查数字列表中是否包含 1
# 列表推导式(new_list = [expression for item in iterable if condition == True])
collection = [1, 2, 3, 4, 5]
[print('列表推导式：', item) for item in collection[-2:]]
print('列表推导式：', [item + 1 for item in collection if item > 2])  # 筛选大于 2 的元素并将符合条件的元素加 1 后放入新列表
print('列表推导式：', [item for item in collection])  # 复制整个列表
# 解包
collection = [1, 2, 3, 4, 5]
(v, *arr) = collection  # * 表示将剩下的元素作为列表赋值到变量
print('unpack', v, arr)
(v1, *arr, v2) = collection
print('unpack', v1, v2, arr)
# 复制
_ = collection.copy()
_ = set(collection)  # 使用具体的类型复制集合
_ = collection[:]  # 使用空索引复制集合

collection = [1, 1, 2, 2, 3, 3]
print('collection count', collection.count(2))  # 统计某个元素在集合中的数量
print('collection index', collection.index(3))  # 获取某个元素在集合中第一次出现的索引

# 列表 list
ls = [1, 2, 3]
_ = ls[0]  # 索引访问
ls.append(4)  # 有序 [1, 2, 3, 4]
ls.append(4)  # 允许重复 [1, 2, 3, 4, 4]
len(ls)  # 获取长度
ls.append(True)  # 列表内可以是任意类型
ls[1:2] = [5]  # 修改
del ls[2:]  # 删除指定索引的内容，没有默认值

def cus_func(n):
    return n - 50

ls.sort(reverse = True, key = cus_func)  # 排序，可选参数 [reverse] 表示降序，key 为自定义排序函数
ls.insert(1, 4)  # 插入
ls.append(4)  # 追加
ls.extend({10: 123})  # 扩展（可以扩展任意可迭代对象）
ls.remove(4)  # 删除（只删除一个）
ls.pop(2)  # 删除（参数为索引，默认值为 -1）
ls.reverse()  # 反转
ls.clear()  # 清空
print('list:', type(ls), ls)

# 元组 tuple
tp = (1)  # 单项的元组需要在元素后面加逗号，这种方式声明的不是元组
print('not tuple:', type(tp), tp)
tp = (1,)
print('tuple:', type(tp), tp)

# 集合 set
st = {0, 1, 2, 3}  # 声明一个集合
st.add(4)  # 添加元素
st.add('123')  # 集合内可以是任意类型
st.add(1)  # 重复元素无法再次添加
st.add(True)  # True 被视为与 1 相同
st.add(False)  # False 被视为与 0 相同
st.update((4, 5, 6))  # 批量添加元素
st.remove(4)  # 删除元素
st.discard(5)  # 删除元素
# st.remove(4)  # 报错
st.discard(4)  # 不报错
st.pop()  # 删除一个随机项
# set().pop()  # 空集合会报错
st.clear()  # 清空
print('st:', type(st), st)
# 并集
# update 会更新原集合，没有返回值；union 不更新原集合，会返回与参数的并集
st = {1, 2, 3}
st.update({2, 3, 4})
print('update set:', st)
st = {1, 2, 3}
st2 = st.union({2, 3, 4})
st3 = st | {2, 3, 4}  # union 可以使用 | 运算符代替
print('union set:', st, st2, st3)
# union 操作多个集合
_ = st.union({2, 3, 4}, {3, 4, 5})
_ = st | {2, 3, 4} | {3, 4, 5}
# 与其他类型集合合并
_ = st.union((2, 3, 4))  # 该操作无法使用 | 运算符
# 交集
st2 = st.intersection({2, 3, 4})
st3 = st & {2, 3, 4}
print('intersection set:', st, st2, st3)
# 差集
st2 = st.difference({2, 3, 4})
st3 = st - {2, 3, 4}
# difference_update 方法效果相同，但会更新原集合
print('difference set:', st, st2, st3)
# 对称差集
st2 = st.symmetric_difference({2, 3, 4})
st3 = st ^ {2, 3, 4}
# symmetric_difference_update 方法效果相同，但会更新原集合
print('symmetric difference:', st, st2, st3)

# 字典
# 字典的每一个项都是一个键值对
# 字典的集合特性都应用在键上（键有序、不可重复）
dc = {'name': 'kurt', 'age': 18, 'country': 'china'}  # 声明一个字典
items = dc.items()
keys = dc.keys()
values = dc.values()
print('dictionary items:', items)
print('dictionary keys:', keys)
print('dictionary values:', values)
# 字典索引
# 根据键索引
print('dictionary index:', dc['name'])
# 修改
dc['name'] = 'kurtis'
dc.update({'age': 20, 'action': 'sleep'})
dc.pop('age')  # 删除项
del dc['country']  # 删除项
dc.popitem()  # 删除最后添加的项
dc.clear()  # 清除
print('dictionary items:', items)
print('dictionary keys:', keys)
print('dictionary values:', values)
# 检查是否存在
print('dictionary existence:', 'name' in dc, 'test' in dc)
# 遍历字典
dc = {'name': 'kurt', 'age': 18}
for key in dc: print('dictionary iteration:', key, dc[key])
# for key in dc.keys(): print('dictionary iteration:', key, dc[key])  # 相同
for value in dc.values(): print('dictionary value iteration:', value)
for key, value in dc.items(): print('dictionary item iteration:', key, value)
