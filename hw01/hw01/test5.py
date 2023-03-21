def hailstone(x):
    """Print the hailstone sequence starting at x and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"

    print(x)
    if(x==1):
        return 1
    elif(x%2==0):
        return 1 + hailstone(x//2)
    else:
        return 1 + hailstone(x*3+1)
    

a = hailstone(10)
print("--------")
print(a)