# 异常

try:
    print('do something')
    raise Exception('error')
except Exception as e:
    print(e)
else:
    print('no exception')
finally:
    print('finally do something')
