def fibo(n):
    a,b=0,1
    print(a,b,sep='\n')
    for i in range(3,n+1):
        sum=a+b
        print(sum)
        a,b=b,sum

n=int(input("Enter number of terms:"))
fibo(n)