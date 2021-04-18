'''
    Reusable input validation callbacks across usecases,
    that always return a boolean, 
    follows single responsibility principle of testing one arguement
    at a time, uses guard clauses for validation
'''
def arg1_range(arg1):
    """tests that arg1 is in the interval dictated by the domain
        rules of the usecase

        Parameters
        ----------
        arg1 : int
            in the interval (0,100]
            

        Returns
        -------
        meets_business_rules : bool
            True if arg1 meets the busines rules, otherwise False
    """
    if type(arg1) != int:
        return(False)

    if arg1 <= 0:
        return(False)
    
    if arg1 > 100:
        return(False)

    return(True)