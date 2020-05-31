# Dependencies
import os
import csv
import operator

# Specify the file to read and create lists to save data
election_data_path = os.path.join('C:/','Users/','Administrator/','Documents/','GitHub/','python-challenge/','PyPoll/','Resources/', 'election_data.csv')
voter_id=[]
candidate=[]
different_candidate=[]
candidate_votes={}

# Store the data from the file to the lists
with open(election_data_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader,None)
    
    for row in csvreader:
        voter_id.append(row[0])
        candidate.append(row[2])

# The number of total votes
total_votes=len(voter_id)

# Initialize the number of different candidates found to 0
nFound=0

# Loop through all the votes.
for name in candidate:
    # Set the boolean is_ New_Candidate to True, and change it to False only if the candidate is one already found
    is_New_Candidate=True
    if nFound>0:
        # Compare the current candidate to the candidates already found
        for found_candidate in different_candidate:
            # The current candidate is not a new one, so update the votes he/she has got.
            if name == found_candidate:
                is_New_Candidate=False
                candidate_votes[name]=candidate_votes[name]+1
            
    
    if is_New_Candidate:
        # The current candidate is a new one, so update the different candidates list  and initiaze the votes count
        nFound=nFound+1
        different_candidate.append(name)
        candidate_votes[name]=1

# Output results to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for name in different_candidate:
    print(f"{name}: {candidate_votes[name]*100/total_votes:6.2f}% ({candidate_votes[name]})")
print("-------------------------")
print(f"Winnder: {max(candidate_votes.items(), key=operator.itemgetter(1))[0]}")
print("-------------------------")

# Output results to a new file
output_file = os.path.join('C:/','Users/','Administrator/','Documents/','GitHub/','python-challenge/','PyPoll/','analysis/',"election_data_output.csv")
with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Election Results"])
    writer.writerow(["-------------------------"])
    writer.writerow([f"Total Votes: {total_votes}"])
    writer.writerow(["-------------------------"])
    for name in different_candidate:
         writer.writerow([f"{name}: {candidate_votes[name]*100/total_votes:6.2f}% ({candidate_votes[name]})"])
    writer.writerow(["-------------------------"])
    writer.writerow([f"Winnder: {max(candidate_votes.items(), key=operator.itemgetter(1))[0]}"])
    writer.writerow(["-------------------------"])
