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
        
            
            
        for set1 in range(1,10):
            for set2 in multi:
                a = set1*set2
                print(set2, "*", set1, "=", str(a).rjust(2,' ') ,end = '   ')
            print()
        
        break
            
