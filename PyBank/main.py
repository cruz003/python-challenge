import os
import csv

csvpath = os.path.join('budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)

#skip header row
    header = next(csvreader)
    row_count = 0
    total = 0

    for row in csvreader:
        month = str(row[0])
        profit_loss = int(row[1])
        total += profit_loss
        row_count += 1

    avg_change = total/row_count

    print("Financial Analysis")
    print("------------------")
    print("Total Months: " + str(row_count))
    print("Total: $" + str(total))

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)

#skip header row
    header = next(csvreader)

    month = []
    profit_loss = []
    calc_change = []

#Read CSV and store values in List    
    for row in csvreader:
        month.append(row[0])
        profit_loss.append(int(row[1]))

#Calculate Profit increase/decrease between months and store in calc_change listcd 
    for i in range(1, row_count):
        calc_change.append(int(profit_loss[i]) - int(profit_loss[i-1]))

    print("Average Change: $"  + str(sum(profit_loss)/row_count))
    print("Greatest Increase in Profits: " + (str(month[calc_change.index(max(calc_change))])) + "  $" + str(max(calc_change)))
    print("Greatest Decrease in Profits: " + (str(month[calc_change.index(min(calc_change))])) + " $" + str(min(calc_change)))