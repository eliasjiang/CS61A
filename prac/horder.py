
def identity(n):
    return n

def square(n):
    return n*n
def triple(n):
    return 3*n

def summariation(n,item):
    total,k = 0,1
    while k <= n:
        total,k = total+item(k),k+1
    return total

def sum1(n):
        return summariation(n,square)

def sum2(n):
        return summariation(n,triple)


def adderCtr(k):
    def adder(n):
        return n+k
    return adder;

def adderByThree(n):
    return adderCtr(3)(n)

