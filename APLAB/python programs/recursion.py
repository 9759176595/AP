def Fibo(n):
    if n==0:
        return 1
    if n==1:
        return 1
    return Fibo(n-1)+Fibo(n-2)
t=eval(input(print("enter the value for fibonacci:")))
print("The output is =",Fibo(t))
