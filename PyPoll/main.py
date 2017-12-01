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

#Dictionary for k:v pairs
d = {}

#This loop must be outside numToCheck for loop to count all .csv items
for row in candidateList:
	
	if row not in uniqueList:
		uniqueCount = candidateList.count(row)
		uniqueList.append(row)
		d[row]=uniqueCount

#max() method plus dictionary access to pull k:v pairs
totalVotes = len(candidateList)
winner = max(d, key=d.get)

#-------------------------------------------------------
#Terminal output of results

print("Election Results")
print("----------------------------")
print("Total Votes: " + str(totalVotes))
print("----------------------------")
for candidate in d:
	percent = round(d[candidate]/totalVotes * 100,2)
	print(candidate +": "+ str(percent) +"%" +" ("+str(d[candidate]) +")")
print("----------------------------")
print("Election winner: " + winner)
print("----------------------------")

#-------------------------------------------------------
#Save results to file

with open('output.txt', 'w+') as file:
	file.write("Election Results\n")
	file.write("----------------------------\n")
	file.write("Total Votes: " + str(totalVotes)+"\n")
	file.write("----------------------------\n")
	for candidate in d:
		percent = round(d[candidate]/totalVotes * 100,2)
		file.write(candidate +": "+ str(percent) +"%" +" ("+str(d[candidate]) +")\n")
	file.write("----------------------------\n")
	file.write("Election winner: " + winner+"\n")
	file.write("----------------------------\n")
	file.close()

#-------------------------------------------------------
#Debugging

#load only first file (or portion of first file) to speed up debugging/testing
#fileNumber = ['1']

#for x in range (1,20):
	#print (candidateList[x])

#print(uniqueList)


#pseudocode for unqiue vote count per candidate 
'''
for each unique item in unique list
	count the occurences of said unique item in individual counters
	
	then calculate percentage in relation of total votes

	then calcuate winner
''' 
	

