s=input("Enter a string:")
d={}
for x in s:
    if x not in d:
        d.update({x:1})
    else:
        d[x]=d[x]+1
for x in d:
    if d[x]>1:
        print(x,"count=",d[x])
