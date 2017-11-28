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

    with open(budgetCSV,'r') as csvFile:

        csvreader = csv.reader(csvFile, delimiter=',')

        # Skip header row in the .csv
        next(csvreader, None)

        for row in csvreader:
            date.append(row[0])
            revenue.append(row[1])

            totalRevenue = totalRevenue + int(row[1])
            if not row[0] in monthList:
                #First three characters = month
                #Split then, reference first element
                #monthList.append(row[0].split("-", 1)[0])
                monthList.append(row[0])
                monthTotal = monthTotal + 1

    combinedBudgetCSV = zip(date, revenue)

    with open(newBudgetCSV, 'w', newline='') as csvFile:

        csvWriter = csv.writer(csvFile, delimiter=',')

        # Write Headers into file
        csvWriter.writerow(["Date","Revenue"])

        # Write the zipped lists to a csv
        csvWriter.writerows(combinedBudgetCSV)

print (monthList)

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(monthTotal))
print("Total Revenue: $" + str(totalRevenue))
print("Average Revenue Change: $")
print("Greatest Increase in Revenue: ")
print("Greatest Decrease in Revenue: ")
print("----------------------------")
    		
