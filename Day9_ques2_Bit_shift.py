n = int(input("Enter a number : "))

odd = n & 0xAA
even = n & 0x55

print(odd)
print(even)

ans = odd>>1 | even<<1

print(ans)