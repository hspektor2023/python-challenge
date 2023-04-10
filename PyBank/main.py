# Modules
import os
import csv

# Set path for file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Set variables
counter = 0
total_fund_balance = 0
total_changes = 0
average_change = 0
change = 0
greatest_increase = 0
greatest_decrease = 999999999
greatest_increase_month = 0
greatest_decrease_month = 0

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
        #print(row)
        counter+=1
        total_fund_balance+=float(row[1])
        total_changes+=float(row[2])
        change = float(row[2])
        if change > greatest_increase:
            greatest_increase = change
            greatest_increase_month = str(row[0])

        if change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_month = str(row[0])

    # Calculate the average change
    average_change = total_changes / (counter - 1)
    
    # Print the results
    print("Total Months: " + str(counter))
    print("Total: " + "$" + str(round(total_fund_balance)))
    print("Average Change: " + "$" + str(average_change))
    print("Greatest Increase in Profits: " + str(greatest_increase_month) + " (" + "$" + str(round(greatest_increase)) + ")")
    print("Greatest Decrease in Profits: " + str(greatest_decrease_month) + " (" + "$" + str(round(greatest_decrease)) + ")")


lines = ['Total Months: 86' , 'Total: $22564198', 'Total Votes: 369711', 'Average Change: $-8311.105882352942', 'Greatest Increase in Profits: 16-Aug ($1862002)', 
         'Greatest Decrease in Profits: 14-Feb ($-1825558)']

# Specify the file to write to
output_path = os.path.join("analysis", "pybank.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as f:
    f.write('\n'.join(lines))




