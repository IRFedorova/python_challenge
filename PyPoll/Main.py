# Dependancies
import csv

# Files to load and output
file_to_load = "Resources/election_data_1.csv"
file_to_output = "Analysis/election_analysis_1.csv"

#Total vote counter
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0

#Read the in csv and conver in into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.DictReader(election_data)
    
    # for each row ...
    for row in reader:
        
        #add to the file vote count
        total_votes = total_votes + 1
        
        #Extract the candidate name from each row
        candidate_name = row["Candidate"]
        
        #if the candidate does not match any existing candidates...
        if candidate_name not in candidate_options:
            
            #add it to the list of candidates in the running
            candidate_options.append(candidate_name)
            
            #beging tracking that candidate's voter count
            candidate_votes[candidate_name] = 0
            
        #add a vote to that candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
            
        
# print the result and export the data to the TEXT file  
with open(file_to_output, "w") as txt_file:
            
    #print the final result ON THE SCREEN
    election_results = (
        f"\n\nElection Results\n"
        f"....................\n"
        f"Total Votes: {total_votes}\n"
        f"....................\n"
    )
    print(election_results)
    
    #SAVE the final vote cout to the TEXT FILE
    txt_file.write(election_results)
    
    #Determine the winner by loopeing through the counts
    for candidate in candidate_votes:
        
        #retrive the vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100
        
        #determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
            
        #print each candidate's vote count and percentage on the SCREEN
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output)
        
        #SAVE each candidate voter count and percentage to Text File
        txt_file.write(voter_output)
        
    
    #print the winning candidate 
    winning_candidate_summary = (
        f"........................\n"
        f"Winner: {winning_candidate}\n"
        f"........................\n"
    ) 
    #printing on the screen
    print(winning_candidate_summary)
   
        
    #Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
    
   


            
        
        
        
        
        
            
        
        