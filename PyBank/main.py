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
            #revenue.append(int(row[1])) results in type error for int + str 
            totalRevenue = totalRevenue + int(row[1])

            if row != 1 & referenceChangeFlag == False:
                #Skip first item in revenue list to prevent index/out of bounds error
                referenceChange = int(row[1])
                    #set first value of revenue list to be reference
                referenceChangeFlag = True
                
            elif row != 1:
                runningChange = referenceChange - int(row[1])
                averageRevenueChange.append(runningChange) 

                if runningChange < greatestDecreaseRevenue: 
                    greatestDecreaseRevenue = runningChange
                    greatestDecreaseRevenueDate = row[0]
                elif runningChange > greatestIncreaseRevenue:
                    greatestIncreaseRevenue = runningChange
                    greatestIncreaseRevenueDate = row[0]

    #Zip function to Save the combined CSV data to a new file; not required
    #combinedBudgetCSV = zip(date, revenue)

#period definition for output, i.e. what is the definition of one period for the analysis? 

'''
#psuedocode for period definition (not implemented)

userinput [y/n] to use 12 months as period definition
output:
    Total months 
    Period count 
        periodlen(date)/12 (rounded?)
    average revenue change (per period, averaged together)
    greatest increase in revenue, month/year, period count, $ increase
    greatest increase in revenue, month/year, period count, $ decrease

'''

monthTotal=len(date)
print("Using total number of months as period for analysis...")
averageRevenue = round(sum(averageRevenueChange)/monthTotal)

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(monthTotal))
print("Total Revenue: $" + str(totalRevenue))
print("Average Revenue Change: $" + str(averageRevenue))
print("Greatest Increase in Revenue: " + str(greatestIncreaseRevenueDate) + " ($"+str(greatestIncreaseRevenue)+")")
print("Greatest Decrease in Revenue: " + str(greatestDecreaseRevenueDate) + " ($"+str(greatestDecreaseRevenue)+")")
print("----------------------------")

#-------------------------------------------------------
#Write terminal results to new file

with open('output.txt', 'w+') as file:
    #Triple quotes to enclose multiple lines in print statement is possible; specifics for variables needed to use correctly
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write("Total Months: " + str(monthTotal)+ '\n')
    file.write("Total Revenue: $" + str(totalRevenue)+ '\n')
    file.write("Average Revenue Change: $" + str(averageRevenue)+ '\n')
    file.write("Greatest Increase in Revenue: " + str(greatestIncreaseRevenueDate) + " ($"+str(greatestIncreaseRevenue)+")\n")
    file.write("Greatest Decrease in Revenue: " + str(greatestDecreaseRevenueDate) + " ($"+str(greatestDecreaseRevenue)+")\n")
    file.write("----------------------------\n")
    file.close()

#-------------------------------------------------------
#Save the combined CSV data to a new file - not required 

#with open(newBudgetCSV, 'w', newline='') as csvFile:

    #csvWriter = csv.writer(csvFile, delimiter=',')

    # Write Headers into file

    #csvWriter.writerow(["Date","Revenue"])

    # Write the zipped lists to a csv

    #csvWriter.writerows(combinedBudgetCSV)

#-------------------------------------------------------
#Debugging

#print(type(row))
#print(averageRevenueChange)

