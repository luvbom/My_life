def power(n,x):
    if x == 0:
        return 1
    else:
        return n*power(n,x-1)
    
print(power(3,3))

"""정답
def power(x, n):
    if n == 0:
        return 1
    elif (n%2) == 0:
        return power(x*x, n//2)
    else:
        return x*power(x*x, (n-1)//2)"""
