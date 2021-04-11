while True:
    s,e = input("").split(' ')
    s = int(s)
    e = int(e)

    if s<=1 or s>9 or e<=1 or e>9:
        print("INPUT ERROR!")
    else:
        multi = []

        if s>=e:
            for i in range(e,s+1):
                multi.append(i)
            multi.reverse()
            
        elif e>s:
            for j in range(s,e+1):
                multi.append(j)
        
            
            
        for set1 in multi:
            for set2 in range(1,10):
                a = set1*set2
                print(set1, "*", set2, "=", str(a).rjust(2,' ') ,end = '   ')
                if set2%3 ==0:
                    print()
            print()
        
        break
            
