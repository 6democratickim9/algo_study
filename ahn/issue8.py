def solution():
    n, m = map(int, input().split(' '))
    
    if n > 100 or n < 0:
        print("INPUT ERROR!")
        return
    
    if m == 1:
        for x in range(1, n+1):
            print("*" * x)
    elif m == 2:
        for y in range(n, 0, -1):
            print("*" * y)
    elif m == 3:
        for z in range(1, n+1):
            print(" " * (n-z) + "*" * (2*z -1))
    else: 
        print("INPUT ERROR!")
        return

    
solution() 