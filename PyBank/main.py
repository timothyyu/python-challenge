import csv
import os

fileNumber = ['1', '2']

for numToCheck in fileNumber:

    budgetCSV = os.path.join('raw_data', 'budget_data_' + numToCheck + '.csv')

    newBudgetCSV = os.path.join('raw_data', 'budget_data_combined.csv')
    
    date=[]
    revenue=[]

    with open(budgetCSV,'r') as csvFile:

        csvreader = csv.reader(csvFile, delimiter=',')

        # Skip header row in the .csv
        next(csvreader, None)

        for row in csvreader:
            date.append(row[0])
            revenue.append(row[1])

    combinedBudgetCSV = zip(date, revenue)

    with open(newBudgetCSV, 'w', newline='') as csvFile:

        csvWriter = csv.writer(csvFile, delimiter=',')

        # Write Headers into file
        csvWriter.writerow(["Date","Revenue"])

        # Write the zipped lists to a csv
        csvWriter.writerows(combinedBudgetCSV)

#print (combinedBudgetCSV)
#print (date[1] + " " + revenue[1])
    	
    		
