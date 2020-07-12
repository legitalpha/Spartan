x = int(input("Enter a number : "))
t = x>>4
y = t & 0x0F
print("MSB of",x,"is",y)
