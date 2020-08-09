x = int(input("Enter a number : "))
def josephusProblem(x):
    y = bin(x)
    z = y.replace("0b","")

    lst = list(z)

    x= lst[0]

    lst.remove(lst[0])

    lst.append(x)

    s = ""
    for ele in lst:
        s += ele

    i = int(s,2)
    print(i,"is the safest position")

josephusProblem(x)