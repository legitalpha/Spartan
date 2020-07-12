n = int(input("Enter a number : "))

m = n>>4
l = n<<4

msb = m & 0x0f
lsb = l & 0xf0

print(msb+lsb)