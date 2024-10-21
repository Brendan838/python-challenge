#importing modules

import csv
import os

#starter code for creating variables to store file names, paths, and locations.

file_to_load = os.path.join("Resources", "election_data.csv") 
file_to_output = os.path.join("Analysis", "election_analysis.txt")  

#creating counter for votes
total_votes = 0 

#creating empty dictionary we will add candidate keys and values to. 
candidates = {}

with open(file_to_load) as election_data:
    #read file and skip first row (headers)
    reader = csv.reader(election_data)
    header = next(reader)
    
    for row in reader:
        #add vote to vote counter
        total_votes+= 1

        #if the candidate exists inside of candidate dictionary, add to their total, 
        # otherwise create new candidate with one vote. 
        if candidates.get(row[2]):
           candidates[row[2]] += 1
        else:
           candidates.update({row[2]: 1}) 


#putting output into formatted text string "output" variable
#1. total votes is just our counter variable
#2. I did a fancy list comprehension to display candidates, % of vote and votes. 
#   This put all of the candidates in a list, and then joined them on chr(10), which the character index of 
#   \n which is the newline character, ensuring each candidate displays on a new line. 
#    Rounded all the percentages to 3 decimal places. 
#3. Found the  candidate inside our dictionary with the most votes. This is using the max function, but there is an extra
#   step/parameter you can put in that tells max() how to compare the values which is useful for when you are
#   looking at dictionaries instead of lists. In this case, I put key =  which will compare candidate's vote totals.

output = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
{chr(10).join(f"{can}: {round((candidates[can]/total_votes)* 100,3)}% ({candidates[can]})" for can in candidates)}
-------------------------
Winner: {max(candidates,key= candidates.get)}
-------------------------
"""


#write to text file in Analysis folder
#printed to terminal


with open(file_to_output,"w") as file:
     file.write(output)

print(output)       