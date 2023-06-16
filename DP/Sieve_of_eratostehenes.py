def sieve(num):
    check_p=[True]*(num)
    check_p[0]=check_p[1]=False
    
    p=2
    while p*p<=num:
        if check_p[p]:
            for i in range(p*p,num,p):
                check_p[i]=False
        p+=1
    primes=[]
    for i in range(2,num):
        if check_p[i]:
            primes.append(i)
    return primes
            
limit=10
print(f"the total prime are an the list is {sieve(limit)}")