sum=0
def number(n):
    if n<=0:
        return 0
    return n+number(n-1)

    
print(number(5))