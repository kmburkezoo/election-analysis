# Data Needed
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4.Percentage of votes each candidate won
# 5. The winner of the election based on popular vote

# Add dependencies
import csv
import os
# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a variable to save analysis file to path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# To do: read and analyze data here
# Initialize total vote counter
total_votes = 0

# Identify andidate options
candidate_options = []

# Create dictionary to hold vote count for each candidate
candidate_votes = {}

# Create winning candidate and count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Print the header row to check if correctly skipped
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:
        # print(row)
        # Add to total vote count
        total_votes += 1 

        # Print candidate name from each row
        candidate_name = row[2]

        # Add candidate name to options list if not already on it
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            # Begin tracking candidate's vote
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] +=1

#Determine each candidate's vote percentage
# Iterate for candidate names
for candidate_name in candidate_votes:
    # Retrieve candidate's total votes
    votes = candidate_votes[candidate_name]
    # Calculate vote percentage
    vote_percentage = float(votes) / float(total_votes) * 100
    # Print candidate name and vote percentage
    # print(f'{candidate_name} received {vote_percentage:.1f}% of the vote')

    # Print each candidate's name, vote, and percentage
    print(f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')

    # Determine winning candidate
    # Determine if this candidate's count is greater than winner so far
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # update winning count
        winning_count = votes
        # update winning percentage
        winning_percentage = vote_percentage
        # update winning candidate
        winning_candidate = candidate_name

#summary
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

# Print total votes
# print(total_votes)

# Print candidate options
# print(candidate_options)

# Print votes per candidate
# print(candidate_votes)

# Close file
election_data.close()



# # Use the open statement to open the file as a text file.
# with open(file_to_save, "w") as txt_file:

#     # Write three counties to file
#     txt_file.write("Counties in the Election\n---------------------\nArapahoe\nDenver\nJefferson")

# # Close file
# txt_file.close()