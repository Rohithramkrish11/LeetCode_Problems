import math
def power_reverse(n):
    rev=0
    num=n
    while n>0:
        m=n%10
        rev=rev*10+m
        n=n//10
    return(pow(num,rev)%(pow(10,9)+7))
num = int(input("Enter a number: "))
s=power_reverse(num)
print(f"power is {s}")

