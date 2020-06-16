num=7
x=num
for i in range(1,6,1):
    num=num-1
    for j in range(1,num,1):
        print("*",end=" ")
        x=num-1
    print()
        
num=7
x=num
for i in range(1,6,1):
    num=num+1
    for j in range(1,num,1):
        print("*",end=" ")
        x=num+1
    print()

#################
num=1
x=num
for i in range(1,5,1):
    num=num+1
    for j in range(1,num,1):
        print(j,end=" ")
        x=num+1
    print()
num=5
x=num
for i in range(1,5,1):
    num=num-1
    for j in range(1,num,1):
        print(j,end=" ")
        x=num-1
    print()
    
