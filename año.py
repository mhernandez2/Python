year=int(raw_input("anio"))
if 1982<=year and year<=2048:
    a=year%19
    b=year%4
    c=year%7
    d=(19*a+24)%30
    e=(2*b+4*c+6*d+5)%7
    n=22+d+e

    if 31<=n:
        A=n-31
        print A
else:
    print "error"
          
        
            
