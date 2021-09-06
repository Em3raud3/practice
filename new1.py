
def fib(num):
    a, b = 0, 1
    res = list()
    for i in range(num):
        res.append(a)
        a, b = b, a + b

    return res


print(fib(10))
