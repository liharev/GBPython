# Homework 5.7
import json
with open("Homework_5.7.txt") as myfile:
    finres = {}
    averageprofit = {}
    jsonlist =[]
    allprofit = 0
    avgprofit = 0
    profitable = 0
    for str in myfile:
        firm, ownership, revenue, losses = str.split()
        revenue = int(revenue)
        losses = int(losses)
        finres[firm] = revenue-losses
        if revenue >= losses:
            allprofit += revenue-losses
            profitable += 1
    avgprofit = allprofit/profitable
    averageprofit["average_profit"] = avgprofit
    jsonlist.append(finres)
    jsonlist.append(averageprofit)
with open("homework_5.7.json", "w") as output:
    json.dump(jsonlist, output)
print("Конец программы!")