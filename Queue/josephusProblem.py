n,k = map(int,input("Enter n,k : ").split())
q = [i for i in range(1,n+1)]
while(n!=1):
    tmp=k%len(q)
    print(q.pop(tmp-1)," Eliminated", end=" ")
    q = q[k-1:] + q[:k-1]
    print(q)
    n -= 1
print("The winner is {}".format(q[0]))
