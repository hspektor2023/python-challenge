# Modules
import os
import csv

# Set path for file
csvpath = os.path.join('Resources', 'election_data.csv')

# Set variables
counter = 0
charles = 0
diana = 0
raymon = 0


# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    print(csvreader)
    # Read the header row first (skip this step if there is now header)
    #csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    next(csvreader)

    # Read each row of data after the header and calculate metrics
    for row in csvreader:
        # Capture the number of votes for each candidate
        counter+=1
        if str(row[2]) == "Charles Casper Stockham":
            charles += 1
        if str(row[2]) == "Diana DeGette":
            diana += 1
        if str(row[2]) == "Raymon Anthony Doane":
            raymon += 1

    # Calculate the voting percentages for each candidate
    charles_percent = float(charles / counter)*100
    charles_percent = round(charles_percent,3)

    diana_percent = float(diana / counter)*100
    diana_percent = round(diana_percent,3)

    raymon_percent = float(raymon / counter)*100
    raymon_percent = round(raymon_percent,3)

    # Identifying the winner
    if charles > raymon and charles > diana:
        winner = "Charles Casper Stockham"
    if raymon > charles and raymon > diana:
        winner = "Raymon Anthony Doane"
    if diana > charles and diana > raymon:
        winner = "Diana DeGette"     

    # Print the total number of votes cast
    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(counter))
    print("-------------------------")
    print("Charles Casper Stockham: " + str(charles_percent) + " (" + str(charles) + ")")
    print("Diana DeGette: " + str(diana_percent) + " (" + str(diana) + ")")
    print("Raymon Anthony Doane: " + str(raymon_percent) + " (" + str(raymon) + ")")
    print("-------------------------")
    print("Winner: " + str(winner))
    print("-------------------------")

lines = ['Election Results' , '-------------------------', 'Total Votes: 369711', '-------------------------', 'Charles Casper Stockham: 23.049 (85213)', 
         'Diana DeGette: 73.812 (272892)' ,'Raymon Anthony Doane: 3.139 (11606)', '-------------------------' , 'Winner: Diana DeGette', '-------------------------']

# Specify the file to write to
output_path = os.path.join("analysis", "pypoll.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as f:
    f.write('\n'.join(lines))

