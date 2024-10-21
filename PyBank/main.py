# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Counter Variables
total_months = 0
total_net = 0


#tracking prior row to do change calculation
last_month_profit = 0

#Two empty lists we will store change data and month info inside of with our loop
changes = []
month = []


# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)
 
    for row in reader:
        total_months += 1
        pnl = int(row[1])
        total_net += pnl
        #establishing our current profit into a variable, adding row data to our counter variables above. 
        if last_month_profit: # I originally store this as a Boolean, since we don't want to add the first rows change into our calculations. 
           change = pnl - last_month_profit
           changes.append(int(change)) #adding value to our changes list
           month.append(str(row[0])) #adding month info to our months list
  
        last_month_profit = int(row[1])
        #changing this row to the last month profit value before continuing the loop. 


      
#Reading both lists to get our greatest increases and decreases

greatest_inc = max(changes)
greatest_inc_month = month[changes.index(greatest_inc)]
greatest_dec = min(changes)
greatest_dec_month = month[changes.index(greatest_dec)]
average = sum(changes)/len(changes)

#Chose to put all of the outputs in a multi line f string

output = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_net}
Average Change: ${round(average,2)}
Greatest Increase in Profits: {greatest_inc_month} (${greatest_inc})
Greatest Decrease in Profits: {greatest_dec_month} (${greatest_dec})
"""

#printing, and putting the output into a file inside the analysis folder
print(output)

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)


