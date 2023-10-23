import os
import csv

# Path to collect data from the resources folder and export data to text file
poll_csv = os.path.join('Resources', 'election_data.csv')
file_to_output = os.path.join("analysis", "poll_analysis.txt")

#initial calculations for votes and candidates name
vote_total = 0
candidate = ""

#list for storing values for candidates and vote calculation
final_list = {}

#values for calculation of winner
winner_votes = 0
winner_name = ""
    
#Read the CSV file
with open(poll_csv, 'r') as csvfile:

    #splitting the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #skipping the header row
    next(csvreader)

    for row in csvreader:
    
        #Row counter = number of votes
        vote_total +=1
        
        # Adding/update candidates and vote count to dictionary final_list
        candidate = row[2]
        if candidate in final_list:
            final_list[candidate] += 1
        else:
            final_list[candidate] = 1

#for printing inital result 
print(f"```text")
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {vote_total}")
print(f"----------------------------")

#for printing the text file ouput_1 (output part 1)
output_1 = (
    f"```text\n"
    f"Election Results\n"
    f"----------------------------\n"
    f"Total Votes: {vote_total}\n"
    f"----------------------------\n"
    )
with open(file_to_output, "w") as txt_file:
    txt_file.write(output_1)
    
#printing each candidates in % format
for candidate in final_list:

    #printing percentage of first candidates vote
    percentage = (final_list[candidate]/vote_total)*100
    percentage_formatted = "{:.3f}".format(percentage)

    print(candidate + ": " + str(percentage_formatted) + "%" + " (" + str(final_list[candidate]) + ")")
    
    #printing percentage of second candidates vote
    output_2 = (f"{candidate} : {percentage_formatted}% ({final_list[candidate]})\n")

    # Running function to calculate the number of votes and winner
    if final_list[candidate] > winner_votes:
        winner_votes = final_list[candidate]
        winner_name = candidate
    
    # Appending output file with results
    with open(file_to_output, "a") as txt_file:
        txt_file.write(output_2)

# printing final output
output_3 = (
    f"----------------------------\n"
    f"Winner: {winner_name}\n"
    f"----------------------------\n"
    f"```\n"
    )
# Printing results in terminal
print(output_3)
# Appending output file
with open(file_to_output, "a") as txt_file:
    txt_file.write(output_3)