# Data Needed
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4.Percentage of votes each candidate won
# 5. The winner of the election based on popular vote

import csv

import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a variable to save analysis file to path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Open the election results and read the file
with open(file_to_load) as election_data:

    # To do: read and analyze data here
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Print each row in the CSV file
    # for row in file_reader:
    #     print(row)

    # Print the header row to check if correctly skipped
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file, skipping headers: ???


#     # Print file object
#     print(election_data)

# # Close file
# election_data.close()



# # Use the open statement to open the file as a text file.
# with open(file_to_save, "w") as txt_file:

#     # Write three counties to file
#     txt_file.write("Counties in the Election\n---------------------\nArapahoe\nDenver\nJefferson")

# # Close file
# txt_file.close()