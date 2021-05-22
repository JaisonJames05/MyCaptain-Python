terms=int(input("Enter the number of terms for fibonacci series : "))
n1=0 #first term of the series
n2=1 #second term of the series
if terms<=0:
    print("The requested series is not possible")
else:
    print(n1,n2,end=" ")
    for x in range(2,terms):
        new=n1+n2
        print(new,end=" ")
        n1=n2
        n2=new
