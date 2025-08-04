# 函数

def function():
    pass  # pass 表示一个空块

def function(arg, *args):
    print('This is a function')
    print('Argument of this function:', arg)
    print('Dynamic arguments of this function:', args)
    return 'return value'

value = function(1, 2, 3, 4, 5)
print('Return value:', value)

def key_args(arg1, arg2):
    print('arg1:', arg1, ', arg2:', arg2)

key_args(arg2 = 1, arg1 = 2)

def muti_key_args(**kwargs):
    for key, value in kwargs.items():
        print('Keyword argument:', key, value)

muti_key_args(name = 'kurt', age = 18)

def default_argument(arg = 'default'):
    print('Default argument:', arg)

default_argument()

# , / 之前的参数都必须使用位置参数，*, 之后的参数都必须使用关键字参数
def function(x, y, z, /, *, a, b, c):
    pass

def lambda_function(x, y, lam):
    print('Lambda result:', lam(x, y))

lambda_function(1, 2, lambda x, y: x + y)

def module_function():
    print('Function from function module')
