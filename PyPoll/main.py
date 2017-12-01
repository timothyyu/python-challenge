import csv
import os

fileNumber = ['1','2']

#The following variables have to be outside of the for loop below to work
totalVotes = 0
candidateList = []
uniqueList= [] 
uniqueVoteCount = []

for numToCheck in fileNumber:

	electionCSV = os.path.join('raw_data', 'election_data_' + numToCheck + '.csv')

	with open(electionCSV,'r') as csvFile:

		csvreader = csv.reader(csvFile, delimiter=',')

		# Skip header row in the .csv
		next(csvreader, None)

		for row in csvreader:
			candidateList.append(row[2])

for row in candidateList:
	if row not in uniqueList:
		uniqueList.append(row)
'''
for each unique item in unique list
	count the occurences of said unqiue item in individual counters
	
	then calculate percentage in relation of total votes

	then calcuate winner
''' 				
print(uniqueList)

totalVotes = len(candidateList)

print("Election Results")
print("----------------------------")
print("Total Votes: " + str(totalVotes))
print("----------------------------")
print("----------------------------")
print("Election winner: ")
print("----------------------------")

#------------------------------------------------------

#-------------------------------------------------------
#Debugging

#load only first file (or portion of first file) to speed up debugging/testing
#fileNumber = ['1']

#for x in range (1,20):
	#print (candidateList[x])
	

