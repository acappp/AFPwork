def get_profit(costPrice, salePrice, sellAmount):
    costPrice = float(costPrice)
    salePrice = float(salePrice)
    sellAmount = float(sellAmount)
    profit = sellAmount * (salePrice - costPrice)
    return profit


def get_vintage(totalGrapes):
    if totalGrapes > 100:
        vintage = 'Excellent'
        return vintage
    elif totalGrapes > 40 or totalGrapes < 100:
        vintage = "Good"
        return vintage
    elif totalGrapes < 40:
        vintage = "poor"
        return vintage



#   Mainline code begins here
#   INPUT costPrice, salePrice
print("")
print("")
print("--------------------Ramu's vintage calculator--------------------")
costPrice = input("Enter the cost price  ")
salePrice = input("Enter the sales  ")



#   add grapeHarvest to TotalList
#   END FOR
#   FOR each value in TotalList
#  This strips the variables from each line

#   Opens and reads a file you assign it to
#  function does not create a file it only reads already existing ones
#   get grapeHarvest from file
f = open("weekly-harvest", "r")

#   vList and list total as variables
vlist = []
listTotal = []

for grapeHarvest in f:
    grapeHarvest=grapeHarvest.strip('\n')
    grapeHarvest=grapeHarvest.split(' ')

    vname = grapeHarvest.pop(0)
    vlist.append(vname)
    #listTotal.append([vname])

    total = 0
    for i in grapeHarvest:
        total += float(i)

    listTotal.append(total)
    #lti = listTotal.index([vname])
    #listTotal[lti].append(total)
    print(grapeHarvest)

print(vlist)
print(listTotal)

for value in listTotal:
    totalGrapes = totalGrapes + value



# average = totalGrapes / number of vineyards

# lowest = lowest value in TotalList. Min finds lowest value in a list
lowest = min(listTotal)

#   highest = highest value in TotalList. Max finds highest value in a list
highest = max(listTotal)

#   sellAmount = 45% of totalGrapes
sellAmount = totalGrapes * 0.45

#   profit = getProfit(sellAmount, costPrice, salePrice)
profit = get_profit(costPrice, salePrice, sellAmount)

#   vintage = getVintage(totalGrapes)


#   DISPLAY vineyard + lowest, vineyard + highest
vl = vineyard + lowest
vh = vineyard + highest
print(vl, vh)
#   DISPLAY profit, vintage
print(profit, vintage)
#   WRITE average, vineyard + lowest, vineyard + highest and profit to text file

#   END
