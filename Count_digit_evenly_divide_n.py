def count_digits(n):
    s = 0
    num = n
    while n > 0:
        m = n % 10
      
        if m != 0 and num % m == 0:
          s = s + 1
        n = n // 10
    return s
n = int(input("Enter a number "))
s = count_digits(n)
print(f"Number of digits is {s}")