#Josephus Problem using recursion

def josephus(n, k):
    if (n == 1):
        return 1
    else:
        return (josephus(n - 1, k) + k - 1) % n + 1

n = int(input("Enter the number of people in the circle: "))
k = int(input("Skipping sequence: "))

print("The chosen place is ", josephus(n, k))


#This programme is only applicable when n(skipping sequence) = 2.
#bitwise approach
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
