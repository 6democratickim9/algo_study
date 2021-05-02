def stars(p1, p2):

    if p1<=0 or p1>100 or p2<1 or p2>3:
        print("INPUT ERROR!")
        n, m = input("").split(' ')

        n = int(n)
        m = int(m)

        stars(n, m)
            


    else:
        if p2 == 1:
            for i in range(1,p1+1):
                print("*"*i)
            
        elif p2 == 2:
            for i in range(p1, 0, -1):
                print("*"*i)
            

        elif p2 == 3:
            for i in range(1, p1+1):
                print(" "*(p1-i) + "*"*(2*i-1))
            
# n, m = input("").split(' ')

# n = int(n)
# m = int(m)

# stars(n, m)

print("+" + "^")
print("+", "^")
