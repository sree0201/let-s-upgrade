n=int(input("Enter the height of the plane :"))
if (n==1000):
    print("fly the plane")
elif(n<1000):
    print("land the plane")
elif(n>1000 and n<5000):
    print("come down to 1000ft")
elif(n>=5000):
    print("go around and try later. ")
