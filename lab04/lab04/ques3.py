def reverse_recursive(lst):
    """Returns the reverse of the given list.

    >>> reverse_recursive([1, 2, 3, 4])
    [4, 3, 2, 1]
    >>> import inspect, re
    >>> cleaned = re.sub(r"#.*\\n", '', re.sub(r'"{3}[\s\S]*?"{3}', '', inspect.getsource(reverse_recursive)))
    >>> print("Do not use lst[::-1], lst.reverse(), or reversed(lst)!") if any([r in cleaned for r in ["[::", ".reverse", "reversed"]]) else None
    """
    "*** YOUR CODE HERE ***"

    def helper(lst,nlst=[]):
        if(len(lst)==0):
            return lst,nlst
        else:
            nlst.append(lst[-1])
            return helper(lst[0:-1],nlst)
    
    if(len(lst)==0):
        return lst
    elif(len(lst)==1):
        return lst
    
    nlst = []
    lst,nlst = helper(lst,nlst)
    return nlst
    
