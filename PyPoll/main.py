import csv
import os

fileNumber = ['1', '2']

for numToCheck in fileNumber:

	electionCSV = os.path.join('raw_data', 'election_data_' + numToCheck + '.csv')

	totalVotes = 0
	candidateList = []
	unqiueList = [] 

	with open(electionCSV,'r') as csvFile:

		csvreader = csv.reader(csvFile, delimiter=',')

		# Skip header row in the .csv
		next(csvreader, None)

		for row in csvreader:
			candidateList.append(row[2])
	
		#for row in candidateList:
			#if row[2] not in unqiueList:
				#unqiueList.append(row[1])

		totalVotes = len(candidateList)
		print (totalVotes)
#-------------------------------------------------------
#Debugging

for x in range (1,20):
	print (candidateList[x])
	

