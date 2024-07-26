def cdp(m,p):
    n=len(p)
    p.sort()
    k=max(p)
    for i in range(0,n-m+1):
       sub=p[i:i+m]
       mindiff=max(sub)-min(sub)
       if mindiff<k:
           k=mindiff
    return k
arr= [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50] 
m = 7
print("Minimum difference is ",cdp(m,arr))
