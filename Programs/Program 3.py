for i in range(100):
    if len(str(i))==2:
        b = 1
        for j in str(i):
            b = b * int(j)
        print(i,"|",b)