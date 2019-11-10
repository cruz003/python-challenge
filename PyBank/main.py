import os
import csv

#Set input file, assumes same folder location as main.py
csvpath = os.path.join('budget_data.csv')

#Open file for input
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)

#skip header row and set count variables to zero
    header = next(csvreader)
    row_count = 0
    total = 0

#Loop through input file, store each value in a list.  Tabulate the total and increment row_count by one to determine number of months
    for row in csvreader:
        month = str(row[0])
        profit_loss = int(row[1])
        total += profit_loss
        row_count += 1

#Print the headings out to the screen
    print("Financial Analysis")
    print("------------------")
    print("Total Months: " + str(row_count))
    print("Total: $" + str(total))

#open file for input
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)

#skip header row
    header = next(csvreader)

#create empty list to capture change in profits
    month = []
    profit_loss = []
    calc_change = []

#Read CSV and store values in Lists   
    for row in csvreader:
        month.append(row[0])
        profit_loss.append(int(row[1]))

#Loop through to calculate the monthly difference in profits and store in list
    for i in range(1, row_count):
        calc_change.append(int(profit_loss[i]) - int(profit_loss[i-1]))

#print the calculations to screen
    print("Average Change: $"  + str(sum(profit_loss)/row_count))
    print("Greatest Increase in Profits: " + (str(month[calc_change.index(max(calc_change))])) + "  $" + str(max(calc_change)))
    print("Greatest Decrease in Profits: " + (str(month[calc_change.index(min(calc_change))])) + " $" + str(min(calc_change)))

#set file for output, assume same folder as main.py
output_path = os.path.join("pybank_output.csv")

#print location of output file to screen
print(output_path)

# Open the Output file for writing
with open("pybank_output.csv", 'w', newline='') as outfile:

    # Initialize the csv writer to write rows
    csvwriter = csv.writer(outfile, delimiter=',')

    # Write output to file
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(["------------------"])
    csvwriter.writerow(["Total Months: " + str(row_count)])
    csvwriter.writerow(["Total: $" + str(total)])
    csvwriter.writerow(["Average Change: $"  + str(sum(profit_loss)/row_count)])
    csvwriter.writerow(["Greatest Increase in Profits: " + (str(month[calc_change.index(max(calc_change))])) + "  $" + str(max(calc_change))])
    csvwriter.writerow(["Greatest Decrease in Profits: " + (str(month[calc_change.index(min(calc_change))])) + " $" + str(min(calc_change))])

