first_no=eval(input("enter first no:"))
second_no=eval(input("enter second no:"))
limit=int(input("no of fibonacci nos to be print"))
print(first_no,end=" ")
print(second_no,end=" ")
for i in range(limit+1):
    sum=first_no+second_no
    first_no=second_no
    second_no=sum
    print(sum,end=" ")
              
