# 文件 IO

import os

# r - 读取，打开文件读取内容，文件不存在则报错
# a - 追加，打开文件追加内容，文件不存在则创建
# w - 写入，打开文件写入内容，文件不存在则创建（会清空原文件内容）
# x - 创建，创建文件，若文件存在则报错

# t - 将文件作为文本处理
# b - 将文件作为二进制内容处理

# 默认使用系统字符集，需要指定 utf8
file = open('console.py', encoding = 'utf8')
print(file.read())
file.close()

# with 块结束后会自动调用文件对象的 close 方法
with open('console.py', encoding = 'utf8') as f:
    print(f.read(5))  # 读取前五个字符
    print(f.readline(), end = '')  # 读取一行，读取时会保留换行符
    for line in f:
        print(line, end = '')  # 读取所有行

# 检查路径是否存在
if os.path.exists('content.txt'):
    # 删除文件，若不存在则报错
    os.remove('content.txt')

# 创建文件夹
os.mkdir('files')

if os.path.exists('files'):
    # 删除文件夹，若不存在则报错
    os.rmdir('files')
