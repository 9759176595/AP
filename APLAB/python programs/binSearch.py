##Binary:) search
def BinSearch(list,key):
    low=0
    high=len(list)-1
    while low<=high:
        mid=(low+high)//2
        if list[mid]==key:
            return mid
        elif key>list[mid]:
            low=mid+1
        else:
            high=mid-1
    return -1
list=[10,20,30,34,56,78,89,90]
print(list)
key=eval(input(print("enter the no for search")))
x=BinSearch(list,key)
if(x==-1):
    print(key,"is n0t found in list")
else:
    print("element ",key,"is found at ",x+1)
    
