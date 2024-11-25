from functools import reduce


def func1():
    a: int = 3
    print(f'id_1: {id(a)}')
    a += 1
    print(f'id_2: {id(a)}')

    lst: list[int] = [3, 5, 2, 5]
    print(f'id_3: {id(lst)}')
    lst += [43]
    print(f'id_4: {id(lst)}')


def func2():
    result = lambda x, y, c: (x + y) * c
    print(f'result: {result(4, 6, 2)}')


def func3():
    def decorator(func):
        def new_hello(*args, **kwargs):
            print("oooooooooo")
            func(*args, **kwargs)
            print("oooooooooo")

        return new_hello
    @decorator
    def hello(name):
        print(f'Hello {name}')

    hello("Artem")


def func4():
    print(reduce(lambda x, y: x * y, [1, 4, 5, 6, 5]))



def func5():
    for i in range(5):
        yield i
#
# my = func5()
# print(next(my), next(my), next(my))
# print(next(my))
# print(next(my))
# print(next(my))


a = (i ** 2 for i in range(5))
print(next(a))
print(next(a))
print(next(a))


