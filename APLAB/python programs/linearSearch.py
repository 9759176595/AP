def Linear_Search(My_List,key):
    for i in range(len(My_List)):
                   if(My_List[i]==key):
                       print(key,"is found at index",i)
                   break
    return -1
My_List=[12,23,45,67,89]
print("contents of lists are as follows:")
print(My_List)
key=eval(input("enter the n0 to be searched"))
L1=Linear_Search(My_List,key)
if(L1!=-1):
    print(key,"is found at position",L1+1)
else:
    print(key,"is not present in the list")
