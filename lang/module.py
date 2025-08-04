# 模块

import function as fun  # 引入另一个模块并重命名
import data
import platform
from oop import Person  # 仅导入模块中的某一元素

fun.module_function()

print('value of data:', data.value)

print(platform.system())

print(dir(platform))  # 列出模块中的所有函数名

tom = Person('Tom', 22)
