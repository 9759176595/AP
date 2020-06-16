str1=eval(input("enter  a string"))
print("entered string is:",str1)
print("After removing spaces,the string becomes")
for i in str1:
    if i==" ":
        continue
    print(i,end="")
