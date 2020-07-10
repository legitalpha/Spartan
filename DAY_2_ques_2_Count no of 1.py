import re

n = int(input("Enter a number : "))

def count1(n):
    num = bin(n).replace("0b","")
    print(num)
    s = str(num)
    r = re.sub('[0-]',"",s)
    c = len(r)
    print(c)
    return

count1(n)