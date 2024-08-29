def isEven(n):
    return(n%2 ==0)
n = int(input("Enter a number: "))
print("Even" if isEven(n) else "Odd")