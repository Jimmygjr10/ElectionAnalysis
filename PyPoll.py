'''
The data we need to retrieve
1. The total # of votes cast
2. A complete list of candidates who received votes
3. The percentage of votes each candidate won
4. The total numver of votes each candidate won
5. The winner of the election based on popular vote
'''
import csv
import os
fileToLoad = os.path.join("Resources", "election_results.csv") #Indirect Path 
#Assign a variable for the file to load and the path
#fileToLoad = 'Resources\election_results.csv' #This is the direct path 
#Open the election results and read the file
#election_data = open(fileToLoad, 'r')
with open(fileToLoad) as election_data:

    #To do: perform analysis.
    print(election_data)

#CLose the file
#election_data.close()
#fileToSave = os.path.join()
#print(fileToLoad)