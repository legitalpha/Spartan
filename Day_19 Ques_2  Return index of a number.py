lst = []
d = 0
def createList(lst,d):

    elementsInList = int(input("Enter the number of elements in the list : "))
    if elementsInList<=0:
        print("Invalid Input")
        exit()

    for i in range(0, elementsInList):
        ele = int(input())
        lst.append(ele)

    print(lst)

    d = int(input("Enter a number to search in the list : "))
    if d in lst:
        print(True)
        index = lst.index(d)
        print("Index of ",d,"is ",index)
    else:
        print(False)

createList(lst,d)