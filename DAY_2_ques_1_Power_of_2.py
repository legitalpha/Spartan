num = int(input("Enter a number : "))

def power(num):
    m = (num - 1)
    g = num & m

    if g==0:
        print(num,"is power of 2")
    else:
        print(num,"is not a power of 2")
    return

power(num)