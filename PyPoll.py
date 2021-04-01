# 0. The data we need to retrieve.
import csv
import os

# 0.1Assign a variable to load a file from a path.
file_to_load = '/Users/richellelong/Desktop/Election_Analysis/Resources/election_results.csv'

# 0.2 Assign a variable to save a file from a path.
file_to_save = '/Users/richellelong/Desktop/Election_Analysis/Analysis/election_analysis.txt'

# open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Read and print the header row.
    headers = next(file_reader)
    print(headers)


# Open the election results and read the file.


# to do read and analyze data here




# 1. The total number of votes cast
# 2. A complete list of candidates who received votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won
# 5. The winner of the election based on the popular vote.