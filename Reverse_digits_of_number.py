def reverse_digit(n):
    rev=0
    while n > 0:
     m = n % 10
     rev = rev*10+m
     n=n//10
    return rev
n = int(input("Enter a number: "))
rev = reverse_digit(n)
print(f"reversed number is {rev}" )