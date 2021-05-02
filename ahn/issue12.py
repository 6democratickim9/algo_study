import math

def isPrimeNative(num):
    num2 = math.ceil(math.sqrt(num))
    for n in range(2, num2+1):
        if num % n == 0:
            return False
    return True

def solution():
    num_list = list(map(int, input().split(' ')))
    for num in num_list:
        if num == 1:
            print("number one")
            continue
        if isPrimeNative(num):
            print("prime number")
            continue
        print("composite number")

    
solution()