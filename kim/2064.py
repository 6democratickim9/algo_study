def add_bowls():
    bowls =[]
    bowls.append(list(input()))
    for i in range(len(bowls)):
        for idx in range(bowls):
            cnt = 0
            try:
                if idx!=idx-1:
                    cnt+=10
                    continue
                
                else:
                    cnt+=5
            except:
                cnt+=10
                continue

    return cnt

print(add_bowls())