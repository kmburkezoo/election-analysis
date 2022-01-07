# Election Analysis

## Overview
Given voting data in source file, complete an audit for a Colorado election and provide the following results:

1. Total number of votes cast
2. Complete list of candidates who received votes, including breakdown of number of votes received and percentage of total
3. Election winner based on percentage of popular vote
4. List of counties in precinct, along with a breakdown of its number of votes and percentage of total
5. County with largest voter turnout

## Resources
- Source data: [election results csv](Resources/election_results.csv)
- Software:
  - Python 3.7.6
  - Visual Studio Code 1.63.2

## Election Audit Results
1. Total number of votes cast: 369,711
2. Complete list of candidates who received votes, including breakdown of number of votes received and percentage of total

    |Candidate|Votes Won|Percent of Total|
    |---|---|---|
    |Charles Casper Stockham|85,213|23.0%|
    |Diana DeGette|272,892|73.8%|
    |Raymon Anthony Doane|11,606|3.1%|

3. Election winner based on percentage of popular vote: Diana DeGette
4. List of counties in precinct, along with a breakdown of each county's number of votes and percentage of total

    |County|Votes Cast|Percent of Total|
    |---|---|---|
    |Jefferson|38855|10.5%|
    |Denver|306055|82.8%|
    |Arapahoe|24801|6.7%|

5. County with largest voter turnout: Denver

These results are also saved in the included [text file](Analysis/election_analysis.txt).

## Election Audit Summary
The code included in this submission works by looping through the included CSV results file to identify all unique entries in the "county" and "candidate" fields, then tallying the number of rows associated with each. To do this, it assumes the following are true of the source file:
1. Format
    1. The source file is saved as a .csv
    2. The source file has a header row
    3. County is the second value for each row, and candidate is the third
2. Path
    1. The source file is located in a Resources subfolder within the folder that holds the python script
    2. The source file is named "election_results.csv"

If all of these statements remain true for future elections, the script can be copied to a location meeting these specifications and used as-is. It will not be impacted by elections involving a different number of candidates or counties.

If, in future elections, the results are saved in a CSV with a different name or different location relative to the script used to analyze it, the line of code where the file is loaded can easily be modified to account for these differences:
```
# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
```
If the subfolder is not called "Resources", or the source file is not called "election_results.csv", these values can be modified accordingly.

If results for subsequent elections are not presented in the order (Ballot ID,County,Candidate), the following references to the assumed order of values will need to be modified:
```
# Get the candidate name from each row (assumes candidate is third value in each row)
candidate_name = row[2]
```
```
# 3: Extract the county name from each row (assumes county is second value in each row)
county = row[1]
```
If the results are saved in a format other than .csv, more extensive changes may be required. It will likely be easier to convert the file to a .csv format than to update the script to read a different file format.


