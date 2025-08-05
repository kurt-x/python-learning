# 日期时间

import datetime

# 日期时间（精确到微秒）
now = datetime.datetime.now(datetime.timezone.utc)
print(now)
print('year', now.year)
print('month', now.month)
print('day', now.day)
print('week', now.weekday())
print('hour', now.hour)
print('minute', now.minute)
print('second', now.second)
print('microsecond', now.microsecond)

# 创建一个日期
date = datetime.datetime(2000, 7, 16)

# 格式化
print(f'{now.strftime('%a'):30}', '英文星期字符串（短）')
print(f'{now.strftime('%A'):30}', '英文星期字符串（全）')
print(f'{now.strftime('%w'):30}', '星期编号（0-6，0 表示星期日）')
print(f'{now.strftime('%d'):30}', '一个月中的第 x 天（01-31）')
print(f'{now.strftime('%b'):30}', '英文月份字符串（短）')
print(f'{now.strftime('%B'):30}', '英文月份字符串（全）')
print(f'{now.strftime('%m'):30}', '月份编号（01-12）')
print(f'{now.strftime('%y'):30}', '年份（短，不包含世纪）')
print(f'{now.strftime('%Y'):30}', '年份（全）')
print(f'{now.strftime('%H'):30}', '小时（00-23）')
print(f'{now.strftime('%I'):30}', '小时（00-12）')
print(f'{now.strftime('%p'):30}', 'AM/PM')
print(f'{now.strftime('%M'):30}', '分（00-59）')
print(f'{now.strftime('%S'):30}', '秒（00-59）')
print(f'{now.strftime('%f'):30}', '微秒（000000-999999）')
print(f'{now.strftime('%z'):30}', 'UTC偏移量（+0800）')
print(f'{now.strftime('%Z'):30}', '时区（UTC+08:00）')
print(f'{now.strftime('%j'):30}', '一年中的第 x 天（001-366）')
print(f'{now.strftime('%U'):30}', '一年中的第 x 周（00-53，周日作为每周第 1 天）')
print(f'{now.strftime('%W'):30}', '一年中的第 x 周（00-53，周一作为每周第 1 天）')
print(f'{now.strftime('%c'):30}', '本地化日期时间')
print(f'{now.strftime('%C'):30}', '世纪（20，从 00 开始）')
print(f'{now.strftime('%x'):30}', '本地化日期')
print(f'{now.strftime('%X'):30}', '本地化时间')
print(f'{now.strftime('%G'):30}', 'ISO 8601 标准年份')
print(f'{now.strftime('%u'):30}', 'ISO 8601 标准星期编号（1-7）')
print(f'{now.strftime('%V'):30}', 'ISO 8601 标准周编号（01-53）')
print(f'{now.strftime('%%'):30}', '百分号')

print(now.strftime('%Y-%m-%d %H:%M:%S %Z %z'))
