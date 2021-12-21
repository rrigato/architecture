def factory_function1():
    """"""
    print("factory_function1")


def factory_function2():
    """"""
    print("factory_function2")


def factory_function_default():
    """"""
    print("factory_function_default")


router = {
    "one": factory_function1,
    "two": factory_function2,
    "default": factory_function_default
}