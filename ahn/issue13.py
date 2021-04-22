def solution():
    n, m = map(int, input().split(' '))
    
    answer = 0

    for chk in range(n, m+1):
        if decimal[int(chk)]:
            answer += 1
    return answer


LEN = 2000000
decimal = [False] + [True] * LEN
decimal[1] = False
m = int(LEN ** 0.5)
for i in range(2, m+1):
    if decimal[i] == True:
        for j in range(i+i, LEN+1, i):
            decimal[j] = False

print(solution())