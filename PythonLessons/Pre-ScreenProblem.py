# Ark paradigm problems


class ListReverser:
    infoList = []

    def __init__(self, inputList):
        ListReverser.infoList = inputList

    def mirror(self):

        print(ListReverser.infoList[::-1])

    def twoMirror(self):
        number = 0
        first = 0
        second = 0
        counter = 0

        tempIndex = 0
        for number in ListReverser.infoList:
            tempIndex = +2

            first = number
            second = ListReverser.infoList[tempIndex]

            ListReverser.infoList[counter] = second

            ListReverser.infoList[tempIndex] = first

        print(ListReverser.infoList)

    def threeMirror(self):
        number = 0
        first = 0
        second = 0
        counter = 0

        tempIndex = 0
        for number in ListReverser.infoList:
            tempIndex = +3

            first = number
            second = ListReverser.infoList[tempIndex]

            ListReverser.infoList[counter] = second

            ListReverser.infoList[tempIndex] = first

        print(ListReverser.infoList)


# dsdfsdfsdf
my_list = [10, 2, 7, 15, 30]
my_reverser = ListReverser(my_list)
my_reverser.mirror()            
