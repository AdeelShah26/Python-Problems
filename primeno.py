### Program for printing m no of prime no.s
isprime=True
n=2
i=1
m= int(input())
while i<=m:
    for j in range(2,n):
        if(n==2):
            isprime=True
        if(n%j==0):
            n+=1
            isprime=False
            break
        else:
            isprime=True
    if isprime:
        print(n)
        n+=1
        i+=1
