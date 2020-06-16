########### x^2+x+41=T ######
########### CHARLES BABBAGE FUNCTION  FOR SECOND ORDER ########
x=0
print("{}\t{}\t{}\t{}".format("D2","D1","T","X"))
print("--------------------")
for i in range(0,5):
    x=i
    T=(x*x)+x +41
    if(i==0):
        print('\t\t{}\t{}'.format(T,i))
    elif(i>0 and i<2):
        a=((x-1)*(x-1) + (x-1)+41)
        print('\t{}\t{}\t{}'.format(T-(a),T,i))
    else:
        a=((x-1)*(x-1)+(x-1)+41)
        b=((x-2)*(x-2)+(x-2)+41)
        c=(T-a)-(a-b)
        print('{}\t{}\t{}'.format(c,(T-a),T,i))
