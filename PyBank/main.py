import csv
import os

fileNumber = ['1', '2']

for numToCheck in fileNumber:

    budgetCSV = os.path.join('raw_data', 'budget_data_' + numToCheck + '.csv')

    newBudgetCSV = os.path.join('raw_data', 'budget_data_combined.csv')
    
    date=[]
    revenue=[]
    monthList=[]

    monthTotal = 0 
    totalRevenue = 0

    greatestIncreaseRevenue = 0
    greatestDecreaseRevenue = 0
    
    averageRevenue = 0
    runningChange = 0 
    averageRevenueChange=[]
    referenceChangeFlag = False

    with open(budgetCSV,'r') as csvFile:

        csvreader = csv.reader(csvFile, delimiter=',')

        # Skip header row in the .csv
        next(csvreader, None)

        for row in csvreader:
            date.append(row[0])
            revenue.append(row[1])
            totalRevenue = totalRevenue + int(row[1])
            if row != 1 & referenceChangeFlag == False:
                referenceChange = int(row[1])
                referenceChangeFlag = True
            elif row != 1:
                runningChange = referenceChange - int(row[1])
                averageRevenueChange.append(runningChange)
                print(runningChange)

    combinedBudgetCSV = zip(date, revenue)

monthTotal=len(date)

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(monthTotal))
print("Total Revenue: $" + str(totalRevenue))
#print("Average Revenue Change: $" + print(averageRevenueChange))
print("Greatest Increase in Revenue: ")
print("Greatest Decrease in Revenue: ")
print("----------------------------")

with open(newBudgetCSV, 'w', newline='') as csvFile:

    csvWriter = csv.writer(csvFile, delimiter=',')

    # Write Headers into file
    csvWriter.writerow(["Date","Revenue"])

    # Write the zipped lists to a csv
    csvWriter.writerows(combinedBudgetCSV)
