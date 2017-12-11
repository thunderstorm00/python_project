#返回函数
# 高阶函数除了可以接受函数作为参数外，还可以把函数作为返回值
def calc_sum(*args):
    s = 0
    for i in args:
        s += i;
    return s


print(calc_sum(1, 2, 3, 4))

def lazy_sum(*args):
    def calc_sum():
        s = 0
        for i in args:
            s += i;
        return s
    return calc_sum

print(lazy_sum(1,2,3,4,5)())

#闭包：注意到返回的函数在其定义内部引用了局部变量args，
# 所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用
# 所以，闭包用起来简单，实现起来可不容易。
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i * i
        fs.append(f)
    return fs
