# 0. The data we need to retrieve.
import csv
import os

# 0.1Assign a variable to load a file from a path.
file_to_load = '/Users/richellelong/Desktop/Election_Analysis/Resources/election_results.csv'

# 0.2 Assign a variable to save a file from a path.
file_to_save = '/Users/richellelong/Desktop/Election_Analysis/Analysis/election_analysis.txt'

# 1. Initialize a total vote counter. Module 3.5.1
total_votes = 0

# Candidate Option. Module 3.5.2
candidate_options = []
# 1. Declare the empty dictionary. Module 3.5.3; Dictionary 3.2.7
candidate_votes = {}

# Winning Candidate and Winning Count Tracker. Module 3.5.5
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
    
        # Add to the total vote count. Module 3.5.1
        total_votes += 1

        # Print the candidate name from each row. Module 3.5.2; Using Index @3.2.6
        candidate_name = row[2]

        # if the candidate does not match any existing candidate...Module 3.5.2
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list. Module 3.5.2; Using Append @3.2.6
            candidate_options.append(candidate_name) 

            # Begin tracking the candidate's vote count. Module 3.5.3
            candidate_votes[candidate_name] = 0

        # Add a vote to the candidate's count. Module 3.5.3
        candidate_votes[candidate_name] += 1 

# Save the results to our text file. Module 3.6.1
with open(file_to_save, "w") as txt_file:

    #Print the final vote count to the terminal.
    election_results = (f"\nElection Results\n" f"-------------------------\n" f"Total Votes: {total_votes:,}\n" f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file.
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of the vote count. Module 3.5.4., See 3.2.11	
        vote_percentage = float(votes) /float(total_votes) * 100

        # To do:print out each candidate's name, vote count, and percentage of votes to terminal. Module 3.6.2
        candidate_results = (f"{candidate_name}; {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        # Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate.
        # Determine if the votes is gretaer than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true, then set winning count = votes and winning percent = vote_percentage
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
            
    # to do: print out the winning candidate name, vote count, and percentage to terminal.
    winning_candidate_summary = (f"-------------------------\n" f"Winner: {winning_candidate}\n" f"Winning Vote Count: {winning_count:,}\n" f"Winning Percentage: {winning_percentage:.1f}%\n" f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the (winning candidate's result to text file.
    txt_file.write(winning_candidate_summary)

