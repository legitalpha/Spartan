lst = []
def invertList(lst):

    sizeOfList = int(input("Enter the size of the list : "))
    if sizeOfList>0:
        for i in range(0,sizeOfList):
            ele = int(input())
            lst.append(ele)
        print(lst)

        count=0
        invertedList=[]
        for i in lst:
            count-=1
            invertedList.append(lst[count])
        print(invertedList)
    else:
        print("Invalid Input")
invertList(lst)