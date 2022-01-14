from copy import deepcopy

from factory_function_selection import business_rules

def append_default_ruleset(dispatch_router):
    """Mutates the dispatch_router to apply functions for indexes [100,199]
    
        Parameters
        ----------
        dispatch_router: dict
            Where each key is an int and each value is the factory function
            associated with the key
    """
    for int_index in range(0, 200):
        dispatch_router[int_index] = business_rules.factory_function_default 



def append_business_ruleset(dispatch_router):
    """Mutates the dispatch_router to apply a business ruleset for 
        the function selection logic for indexes [100,199]
    
        Parameters
        ----------
        dispatch_router: dict
            Where each key is an int and each value is the factory function
            associated with the key
    """
    for int_index in range(100, 150):
        dispatch_router[int_index] = business_rules.factory_function1 

    for int_index in range(150, 200):
        dispatch_router[int_index] = business_rules.factory_function2 



def factory_dispatch_router():
    """Routes to a factory function based on dict key selected
    
        Returns
        -------
        dispatch_functions: dict
            Where each key is an int and each value is the factory function
            associated with the key
    """
    dispatch_router = {}
    
    append_default_ruleset(dispatch_router=dispatch_router)
    append_business_ruleset(dispatch_router=dispatch_router)

    return(
        deepcopy(
            dispatch_router
        )
    )