a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

count = 0

while a!=0:
    if a%2==1:
        count +=b
        b=b<<1
        a=a>>1
    if a%2==0:
        b=b<<1
        a=a>>1

print("The product of first and second number is ",count)