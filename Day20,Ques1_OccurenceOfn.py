lst = []
sizeOfList = int(input("Enter the size of list : "))
if sizeOfList>0:
    def myList(lst,sizeOfList):
        for i in range(0,sizeOfList):
            ele = int(input())
            lst.append(ele)
        print(lst)

    numberTobeSearched = None

    def countELe(myList,numbertobeSearched):
        myList(lst, sizeOfList)
        numberTobeSearched = int(input("Enter the number to be searched : "))
        i = 0
        for ele in lst:
            if ele==numberTobeSearched:
                i+=1
        print(numberTobeSearched,"Occured",i,"times in the list")

    countELe(myList,numberTobeSearched)
else:
    print("Invalid Input")