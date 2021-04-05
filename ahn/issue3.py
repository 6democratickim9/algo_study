def solution():
    s, e = map(int, input().split(' '))
    
    result = ""
    if s > e:
        o = -1
        e -= 1
    else:
        o = 1
        e += 1
        
    for j in range(s, e, o):
        for i in range(1, 10):
            if j * i >= 10:
                result = result + f"{j} * {i} = {i*j}   "
            else:
                result = result + f"{j} * {i} =  {i*j}   "
            if i % 3 == 0:
                result = result + "\n"
        result = result + "\n"

    print(result)

solution()