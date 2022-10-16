n=int(input("Enter The Range Till Which To Find The Primr Factors Of : "))
for i in range(1,n+1):
    if (i==1):
        print("1 = 1","9It's A Unique Number")
    else:
        c=0
        print(i,end=" = ")
        j=2
        while i!=1:
            if (i%j==0):
                c+=1
                k=0
                i=i//j
                for x in range(2,j):
                    if (j%x==0):
                        k+=1
                if (k==0 and c==1):
                    print(j,end=" ")
                elif (k==0 and c>1):
                    print(" x ",j,end=" ")
            else:
                j+=1
        if (c==1):
            print("(It's A Prime Number")
        else:
            print()
            
