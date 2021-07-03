# PROGRAM TO KNOW IF THE NUMBER IS PRIME OR NOT
# 'prime number can only be divided by 1 or itself'

num = int(input("enter the number you want to check : "))

if num > 1: #if we give 1 then it will print the last else block
    for i in range(2,num): #divide it by 2 next 3 and next 4 
        if num % i == 0: #6%2==0 so its prime so break will be executed
            print('not prime')
            break #if it gets divide by 2 then its not prime
    else:
        print("prime")

else:
    print("not prime")
