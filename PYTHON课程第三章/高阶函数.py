# 既然变量可以指向函数，函数的参数可以接受变量，那么一个函数就可以接受另一个函数作为参数，这种
# 函数就称之为高阶函数
# example:
def add(x, y, f):
    z = f(x)+f(y)
    return z


res = add(3, -6, abs)
print(res)
