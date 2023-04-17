
def find_twoTh(n):
    i = 0
    while(n!=1):
        n = n //2
        i+=1
    return 2**i