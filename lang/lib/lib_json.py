# JSON

import json

content = '{"name":"John", "age":30, "city":"New York"}'

# 将 json 文本解析成字典
parsed = json.loads(content)

print(parsed, type(parsed))

# 将字典转换成 json
parsed = json.dumps(parsed)

print(parsed, type(parsed))

# 美化
print(json.dumps({'name': 'Tom', 'age': 18}, indent = 2, separators = (';', '='), sort_keys = True))
