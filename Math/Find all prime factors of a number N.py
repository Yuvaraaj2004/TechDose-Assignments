n=50
i=1
factorrs=set()
while i*i<=n:
    if n%i==0:
        factorrs.add(i)
        factorrs.add(n//i)
    i+=1
print(factorrs)