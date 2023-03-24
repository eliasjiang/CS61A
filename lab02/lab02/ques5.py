def both_paths(sofar="S"):
    """
    >>> up, down = both_paths()
    S
    >>> upup, updown = up()
    SU
    >>> downup, downdown = down()
    SD
    >>> _ = upup()
    SUU
    """
    "*** YOUR CODE HERE ***"

    print(sofar)

    def up():
        return both_paths(sofar+"U")
    
    def down():
        return both_paths(sofar+"D")

    return up,down