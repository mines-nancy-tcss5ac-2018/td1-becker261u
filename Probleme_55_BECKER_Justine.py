def palindromic(n):
    a=str(n)
    b=a[::-1]
    return (a==b)
    
def inverser(n):
    a=str(n)
    a=a[::-1]
    return(int(a))
    
def test_lychrel(n):
    a=n+inverser(n)
    k=1
    while k<=50:
        if palindromic(a)==True:
            return False
        else:
            a=a+inverser(a)
            k+=1
    return True
        
assert test_lychrel(4994)==True

def solve(n):
    S=0
    for i in range(n+1):
        if test_lychrel(i):
            S+=1
    return S
    
print(solve(10000))
        