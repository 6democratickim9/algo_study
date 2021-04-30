
def prime(m,n):
    pr_cnt=0
    primes =[]
    for idx in range(m,n+1):
        num = idx
        for div in range(1,num+1):
            if m%div==0:
                pr_cnt+=1

                if pr_cnt ==2:
                    primes.append(idx)    

    print(primes)

    return primes

prime(10,100)