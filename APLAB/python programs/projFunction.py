def Calculate_Compound_Interest(p,n,r):
    print('StartBalance\t','\tInterest\t','Ending Balance')
    total=0
    x=r/100
    tot=0
    for i in range(1,n+1):
        z_new=p*(1+x)**i-p
        z_old=p*(1+x)**(i-1)-p
        tot=tot+(z_new-z_old)
        if(i==1):
            print('{0:.2f}\t'.format(p),end='')
            print('\t{0:.2f}\t'.format(z_new-z_old),end='')
            print('\t\t{0:.2f}\t'.format(z_new+p))
        else:
            print('{0:.2f}\t'.format(p+z_old),end='')
            print('\t{0:.2f}\t'.format(z_new-z_old),end='')
            print('\t\t{0:.2f}\t'.format(z_new+p))
        print('Total Interest Deposited :Rs{0:.2f}'.format(tot))
    p=eval(input("enter the principal amount"))
    r=eval(input("Enter the rate of interest"))
    n=eval(input("Enter no of year:"))
    Calculate_Compound_Interest(p,n,r)
