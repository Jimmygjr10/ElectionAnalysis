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
fileToLoad = os.path.join( "Resources", "election_results.csv") #Indirect Path 
#Assign a variable for the file to load and the path
#fileToLoad = 'Resources\election_results.csv' #This is the direct path 
#Open the election results and read the file
#election_data = open(fileToLoad, 'r')
county = []
countyVotes = {}
candidateOptions = []
totalVotes = 0 
candidateVotes = {}
winningCandidate = ""
winningCounty = ""
winningCountyCount = 0
winningCount = 0
winningPercentage = 0
with open(fileToLoad) as election_data:

    #To do: perform analysis.
    #Read the file object with the reader function
    fileReader = csv.reader(election_data)

    #Print the header row.
    #Next allows us to skip the first row and take the headers out 
    headers = next(fileReader)

    # Print each row in the CSV file.
    for row in fileReader:
        #Add to the total vote count
        totalVotes = totalVotes + 1 

        #Print the candidate name from each row 
        candidateName = row[2]
        #Print the county name from each row
        countyName = row[1]
        #Use logical operator to check if the county name is in the county list I created. IF not then append the names to the list 
        if countyName not in county:
            #Adding the county names to the list I created 
            county.append(countyName) 
            #Write a script that initializes the county vote to zero
            countyVotes[countyName] = 0 
            #Add 1 vote to the county everytime it loops through
        countyVotes[countyName] = countyVotes[countyName] + 1
        
        #This creates a list of the candidates and it will only print their name the first times it finds it. Will ignnore the rest 
        if candidateName not in candidateOptions:
        #Add the Candidate name to the candidate list
            candidateOptions.append(candidateName)
        #Begin tracking that candidates vote count. This code sets it to zero. This also declares each candidate as a key in the dictionary
            candidateVotes[candidateName] = 0 
        #Add 1 vote to candidates count everytime it loops through 
        candidateVotes[candidateName] = candidateVotes[candidateName] + 1
    # Determine the percentage of votes for each candidate by looping through the counts.
  

#CLose the file
#election_data.close()
#fileToSave = os.path.join()
#print(fileToLoad)
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
#outFile = open(file_to_save, "w")
with open(file_to_save, 'w') as txtFile:
#Write data to the file 
    electionResults = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {totalVotes:,}\n"
        f"-------------------------\n")
    #print(electionResults, end="")
    # Save the final vote count to the text file.
    txtFile.write(electionResults)
        # Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
    for candidateName in candidateVotes:
    # 2. Retrieve vote count of a candidate. This grabs the value of each key in the dictionary
        votes = candidateVotes[candidateName]
        print(votes)
    # 3. Calculate the percentage of votes.
        votePercentage = float(votes) / float(totalVotes) * 100
    #Format votePercentage to 22 decimal places
        formattedPercentage = format(votePercentage, ".1f" )
    # 4. Print the candidate name and percentage of votes.
        candidateResults = (f"{candidateName}: {formattedPercentage}% ({votes:,})\n")
        txtFile.write(candidateResults)
        # Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count.
        #2. We'll also add a print statement that prints the winning candidate, winning vote count, and winning percentage.
        if (votes > winningCount) and (votePercentage > winningPercentage):
            # 2. If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winningCount = votes
            winningPercentage = votePercentage
            # 3. Set the winning_candidate equal to the candidate's name.
            winningCandidate = candidateName
            #print(f"{candidateName}: {votePercentage:.1f}% ({votes:,})\n")    
    winningCandidateSummary = (
    f"-------------------------\n"
    f"Winner: {winningCandidate}\n"
    f"Winning Vote Count: {winningCount:,}\n"
    f"Winning Percentage: {winningPercentage:.1f}%\n"
    f"-------------------------\n")
    txtFile.write(winningCandidateSummary)
#print(winningCandidateSummary)
        
#print(votes)
#Close File
#outFile.close()