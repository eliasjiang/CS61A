
def wears_jacket_with_if_one(temp,raining):
    if(temp<=60 or raining):
        return True
    else:
        return False

def wears_jacket_with_if_two(temp,raining):
    return temp<= 60 or raining