while True:
    n, m = input("").split(' ')

    n = int(n)
    m = int(m)

    if n > 100 or m > 100:
        print("INPUT ERROR!")

    else:
        for set1 in range(0, n):

            for set2 in range(1, m+1):
                if set1 >= 1:
                    a = m*set1+set2
                    print(a, end=' ')
                else:
                    print(set2, end=' ')

            print()

    break
