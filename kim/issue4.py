while True:

    p, q = input("").split(' ')
    p = int(p)
    q = int(q)

    div = []

    for a in range(0, p+1):
        try:
            if p % a == 0:
                div.append(a)
                
        except:
            if a==0:
                div.append(a)
            else: 
                continue
    

    try:
        if div[q+1] !=0:
            print(div[q])
    except:
        print(div[0])

    break
