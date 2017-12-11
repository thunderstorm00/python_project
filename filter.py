#filter接收一个函数和一个序列，然后根据返回值确定是否保留还是丢弃该元素
def is_odd(n):
    return n %2 == 1

print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7])))
'dfs'.upper()
def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, [
    '435435', '', "", '123'])))

#计算素数的一个方法是埃氏筛法
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break