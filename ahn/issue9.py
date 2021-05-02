def solution():
    n = int(input())
    array = [[0 for col in range(n)] for row in range(n)]
    m = n
    num = 1
    x = 0
    y = -1
    
    while m > 0:
        for i in range(m):
            y += 1
            array[x][y] = num
            num += 1
        
        m -= 1
        for i in range(m):
            x += 1
            array[x][y] = num
            num += 1
        for i in range(m):
            y -= 1
            array[x][y] = num
            num += 1
        m -= 1
        for i in range(m):
            x -= 1
            array[x][y] = num
            num += 1

    result = ""
    for a in range(n):
        for b in range(n):
            result_num = array[a][b]
            if b+1 == n:
                result = result + f"{result_num}"
            else:
                result = result + f"{result_num} "
        result = result + "\n"
    print(result)

solution()