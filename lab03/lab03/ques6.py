from ques5 import num_eights

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    # value = 0
    # flag = 1
    # for i in range(1,n+1):
    #     value += flag 
    #     if(num_eights(i)!=0 or i%8==0):
    #         flag = -flag
    # return value

    # value
    # index
    # direction
    
    def helper(value,index,direction):
        if(index==n):
            return value
        elif(num_eights(index)!=0 or index%8==0):
            return helper(value-direction,index+1,-direction)
        else:
            return helper(value+direction,index+1,direction)
                          
    

    return helper(1,1,1)