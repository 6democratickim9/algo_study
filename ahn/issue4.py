def solution():
    n, m = map(int, input().split(' '))
    x = 1
    result = ""
    for y in range(m):
        for z in range(n):
            if x % m == 0:
                result = result + f"{x}" + "\n"
            else:
                result = result + f"{x}" + " "
            x += 1
    
    return result


print(solution())        