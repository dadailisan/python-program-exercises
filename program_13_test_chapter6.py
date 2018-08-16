def printTable(data, col, width):
    for k, v in data.items():
        print(k.rjust)

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
prinTable(tableData, 3, 20)


#def printPicnic(itemsDict, leftWidth, rightWidth):
   # print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    #for k, v in itemsDict.items():
#        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
#picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
#printPicnic(picnicItems, 12, 5)
#printPicnic(picnicItems, 20, 6)
