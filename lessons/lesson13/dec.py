def my_dec(fun):
    def wrap(*arg, **kwarg):
        print(f"run {fun.__name__} {arg=} {kwarg=}:")
        result = fun(*arg, **kwarg)
        print(f"end run {fun.__name__} {result=}")
        return result
    return wrap

def symbol(s, c):
    def decorator(fun):
        def wraper(*arg, **kwarg):
            print(s*c)
            result = fun(*arg, **kwarg)
            print(s*c)
            return result
        return wraper
    return decorator


@symbol("-", 30)
@symbol("=", 20)
@symbol("*", 10)
@my_dec
def add(a, b):
    return a+b


# @dec
def div(a, b):
    return a/b
div = my_dec(div)
l1 = symbol("*", 10)
div = l1(div)
l2 = symbol("=", 20)
div = l2(div)
l3 = symbol("-", 30)
div = l3(div)

print(f"{add(1,2)=}")
print(f"{add(3,b=7)=}")
print(f"{div(3,7)=}")
print(f"{div(7, 3)=}")