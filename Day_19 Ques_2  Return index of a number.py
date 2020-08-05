lst = []
numberToBeSearched = 0
def createList(lst,numberToBeSearched):

    elementsInList = int(input("Enter the number of elements in the list : "))
    if elementsInList<=0:
        print("Invalid Input")
        exit()

    for i in range(0, elementsInList):
        ele = int(input())
        lst.append(ele)

    print(lst)

    numberToBeSearched = int(input("Enter a number to search in the list : "))
    if numberToBeSearched in lst:
        print(True)
        index = lst.index(numberToBeSearched)
        print("Index of ",numberToBeSearched,"is ",index)
    else:
        print(False)

createList(lst,numberToBeSearched)
