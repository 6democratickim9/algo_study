import math


def prime_verifier(n, m):
    array = [True for i in range(m+1)]

    for i in range(2, int(math.sqrt(m))+1):
        if array[i] == True:
            
            j = 2
            while i * j <= m:
                
                array[i*j] = False
                j += 1

    return[i for i in range(n, m+1)if array[i]]


n,m = input().split()
n =int(n)
m = int(m)
print(len(prime_verifier(n,m)))

