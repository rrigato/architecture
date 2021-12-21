from copy import deepcopy

def factory_function1():
    """"""
    print("factory_function1")


def factory_function2():
    """"""
    print("factory_function2")


def factory_function_default():
    """"""
    print("factory_function_default")


def factory_router():
    """Routes to function based on dict key selected"""
    complete_routing_dict = {}
    for int_index in range(100, 150):
        complete_routing_dict[int_index] = factory_function1 

    for int_index in range(150, 200):
        complete_routing_dict[int_index] = factory_function2 
    return(
        deepcopy(
            complete_routing_dict
        )
    )