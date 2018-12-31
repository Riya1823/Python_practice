nterms=10
n1=0
n2=1
count=0
if nterms<=0:
    print("Number should be +ve")
elif nterms==1:
    print("Fibonacci number is",nterms,":")
else:
    print("Fibonacci series is:")
    while(count<=nterms):
        print(n1,end=' , ')
        n=n1+n2
        n1=n2
        n2=n
        count+=1
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
       

