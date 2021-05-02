def solution():
    n, k = map(int, input().split(' '))
    half = round(n / 2)
    y = 0
    if half < k:
        print(0)
        return
    for i in range(1, half+1):
        if n % i == 0:
            y += 1
            if y == k:
                print(i)
                return
    print(0)
    
solution() 