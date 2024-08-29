import math
def first_digit(n):
    while n>=10:
      n=n//10
    return n

def last_digit(n):
    return n%10

a = int(input("Enter base value "))
b = int(input("Enter exponent value "))

n = pow(a,b)

print("First digit is", first_digit(n))
print("Last digit is", last_digit(n))