def make_generators_generator(g):
    """Generates all the "sub"-generators of the generator returned by
    the generator function g.

    >>> def every_m_ints_to(n, m):
    ...     i = 0
    ...     while (i <= n):
    ...         yield i
    ...         i += m
    ...
    >>> def every_3_ints_to_10():
    ...     for item in every_m_ints_to(10, 3):
    ...         yield item
    ...
    >>> for gen in make_generators_generator(every_3_ints_to_10):
    ...     print("Next Generator:")
    ...     for item in gen:
    ...         print(item)
    ...
    Next Generator:
    0
    Next Generator:
    0
    3
    Next Generator:
    0
    3
    6
    Next Generator:
    0
    3
    6
    9
    """
    "*** YOUR CODE HERE ***"
    flag = True
    stop = False
    def gen_helper(num_next):
        nonlocal flag
        gen = g()
        lst = []
        for i in range (1,num_next+1):
            try:
                lst.append(next(gen))
            except StopIteration:
                flag = False
        if flag == True: 
            for it in lst:
                yield it

    id = 1

    while(flag):
        ls = []
        for itm in gen_helper(id):
            ls.append(itm)
        if flag:
            yield ls
        id+=1