# Your task is to create a Python script that analyzes the votes and calculates each of the following values:
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote

# Import Libraries
import os
import csv
# Path to collect data from the resources folder
csvpath = os.path.join("Resources", "election_data.csv")
# Path to create and save the txt file to the Analysis folder
txtpath = os.path.join("Analysis", "Output.txt")

# Create variables, empty list, and dictionary
count_votes = 0
candidates = []
candidate_votes = {}
winner_count = 0
winner = ""

# Read in the CSV file
with open(csvpath) as csvfile:
    # Split the data on commas
    csvreader = csv.DictReader(csvfile)
    # Loop trough the rows
    for row in csvreader:
        # Count votes
        count_votes += 1
        # Create a dictionary with candidates and number of votes for each candidate
        candidate = row["Candidate"]
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 1
        candidate_votes[candidate] = candidate_votes[candidate] + 1

# Write the results in the txt file
with open(txtpath,"w") as file:
    
    print(f"Election Results")
    print(f"----------------------------")      
    print(f"Total Votes: {count_votes}")
    print(f"----------------------------") 
    file.write(f"Election Results\n")
    file.write(f"----------------------------\n")
    file.write(f"Total Votes: {count_votes}\n")
    file.write(f"----------------------------\n")
    
    # Calculate and print the candidate, vote percentage and number of votes. Calulcate the winner
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes)/float(count_votes)*100
        if (votes > winner_count):
            winner_count = votes
            winner = candidate
        print(f"{candidate}: {vote_percentage:.3f}% ({votes-1})")
        file.write(f"{candidate}: {vote_percentage:.3f}% ({votes-1})\n")
    
    # Print the winner
    print(f"----------------------------")
    print(f"Winner: {winner}")
    print(f"----------------------------")
    file.write(f"----------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write(f"----------------------------\n")


