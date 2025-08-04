# 面向对象编程

class Person:
    # 定义属性
    name: str

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 方法中的第一个参数是对当前示例的引用，不是必须命名为 self
    def __str__(me):
        return f'{me.name}, {me.age}'

p = Person('kurt', 18)
print(Person.__name__, p)

# 继承
class Student(Person):
    def __init__(self, name, age, year):
        # 调用父类的 init 方法
        # Person.__init__(self, name, age)
        super().__init__(name, age)  # 可以使用 super() 代替具体父类，这时不需要 self 参数
        self.graduation_year = year

# 迭代器
class Numbers:
    def __iter__(self):
        self.n = 1
        return self

    def __next__(self):
        # x = self.n
        # self.n += 1
        # return x

        if self.n <= 5:
            x = self.n
            self.n += 1
            return x
        else:
            # 停止
            raise StopIteration

for n in Numbers():
    print('iterator:', n)
