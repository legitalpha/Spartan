lst = []

elementsInList = int(input("Enter the number of elements in the list : "))
if elementsInList<=0:
    print("Invalid Input")
    exit()

for i in range(0, elementsInList):
    ele = int(input())
    lst.append(ele)

print(lst)

def reverseList(lst):

    newList = []
    for ele in lst:
        newList.append(ele)
    newList.reverse()
    print(newList)

    if lst==newList:
        print(True)
    else:
        print(False)

reverseList(lst)
