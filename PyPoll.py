# Desired deliverables for this code
# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote
# Assign a variable for the file to load and the path.

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#I nitialize a total vote counter.
total_votes = 0

# Initialize a list for all the candidates in file
candidate_options = []

# Initialize vote counter dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    # Print the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
     # Add to the total vote count
        total_votes += 1
     # Print the candidate name from each row 
        candidate_name = row[2]
     #If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
          # Add those names to the candidate list
          candidate_options.append(candidate_name)
          #Make each candidate a key and begin tracking the vote count
          candidate_votes[candidate_name] = 0
        #Add a vote to the candidates count
        candidate_votes[candidate_name] +=1

# Determine the percentage of votes for each candidate by looping through the counts.
for candidate_name in candidate_votes:
     # Get vote count of the candidate from the dictionary
     votes = candidate_votes[candidate_name]
     #Calculate vote percentage
     vote_percentage = float(votes)/float(total_votes)*100
     
     # print out each candidate's name, vote count, and percentage votes

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
     if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name

     #  To do: print out the winning candidate, vote count and percentage to
     #   terminal.
     print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary = (
f"-------------------------\n"
f"Winner: {winning_candidate}\n"
f"Winning Vote Count: {winning_count:,}\n"
f"Winning Percentage: {winning_percentage:.1f}%\n"
f"-------------------------\n")
print(winning_candidate_summary)