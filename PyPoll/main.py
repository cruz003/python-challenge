import os
import csv

#set input file, assumes same folder location as main.py
csvpath = os.path.join('election_data.csv')

#Set votecount variable to count votes, set candidates list to collect unique candidates and set candidate_count dictionary to collect candidates and tally their votes
votecount = 0
candidates =[]
candidate_count = {}

#Loop through file and find unique candiates and add them to the list.  Increment votecount by one for each record to tabulate total number of votes.
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    #Skip the Header Row
    next(csvreader)
    for row in csvreader:
        votecount += 1
        #If unique candidate, add name to candidates list and create Candidate name key in dictionary
        if row[2] not in candidates:
            candidates.append(row[2])
            candidate_count[row[2]] = 0
        #Increment the candidate's vote tally in the dictionary    
        candidate_count[row[2]] = candidate_count[row[2]] + 1


#Print Headings and Summary Outcome
print("Election Results")
print("---------------------")
print("Total Votes: " + str(votecount))
print("---------------------")

#Loop through dictionary and print key value pairs with formatting to screen
for candidate, votes in candidate_count.items():
    print (str(candidate) + ": " + "{0:.0%}".format(votes/votecount) + "   " + str(votes) + " votes")

print("---------------------")

#Determine the winner based on max number of votes and print to screen
winner = max(candidate_count, key=candidate_count.get)
print("Winner: " + str(winner))
print('---------------------')

#Set file for output, assume same folder as main.py
output_path = os.path.join("pypoll_output.csv")

#print location of output file to screen
print("Exported to: " + str(output_path))

# Open the Output file for writing
with open("pypoll_output.csv", 'w', newline='') as outfile:

    # Initialize the csv writer to write rows
    csvwriter = csv.writer(outfile, delimiter=',')

    # Write output to file
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(["---------------------"])
    csvwriter.writerow(["Total Votes: " + str(votecount)])
    csvwriter.writerow(["---------------------"])
    for candidate, votes in candidate_count.items():
        csvwriter.writerow([str(candidate) + ": " + "{0:.0%}".format(votes/votecount) + "   " + str(votes) + " votes"])
    csvwriter.writerow(["---------------------"])
    csvwriter.writerow(["Winner: " + str(winner)])
    csvwriter.writerow(["---------------------"])