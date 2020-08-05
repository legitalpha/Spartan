lst = []

elementsInList = int(input("Enter the number of elements in the list : "))
if elementsInList<=0:
    print("Invalid Input")
    exit()

for i in range(0, elementsInList):
    ele = int(input())
    lst.append(ele)

print(lst)

def replaceNegativeNos(lst):
    for negativeNumber in lst:
        if negativeNumber<0:
            index = lst.index(negativeNumber)
            lst[index]=0
            print(lst)

replaceNegativeNos(lst)
