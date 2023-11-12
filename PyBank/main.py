#Your task is to create a Python script that analyzes the records to calculate each of the following values:
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period

# Import libraries
import os
import csv
# Path to collect data from the resources folder
csvpath = os.path.join("Resources", "budget_data.csv")
# Path to create and save the txt file to the Analysis folder
txtpath = os.path.join("Analysis", "Output.txt")
# Read in the CSV file
with open(csvpath) as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=",")
    # Store the headers
    csv_header = next(csvfile)
    
    # Create empty lists
    months = []
    profit_losses = []
    change = []

    # Append each row to the respective list
    for rows in csvreader:
        months.append(rows[0])
        profit_losses.append(int(rows[1]))

    # Calculate changes in "Profit/Losses"
    for i in range(1, len(profit_losses)):
        change.append((int(profit_losses[i]) - int(profit_losses[i-1])))

    # Print the Results
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {len(months)}")
    print(f"Total: ${sum(profit_losses)}")
    print(f"Average Change: ${round((sum(change) / len(change)), 2)}")
    print(f"Greatest Increase in Profits: {months[change.index(max(change))+1]} ${max(change)}")
    print(f"Greatest Decrease in Profits: {months[change.index(min(change))+1]} ${min(change)}")

    # Output to a text file
    file = open(txtpath,"w")
    file.write(f"Financial Analysis\n")
    file.write(f"----------------------------\n")
    file.write(f"Total Months: {len(months)}\n")
    file.write(f"Total: ${sum(profit_losses)}\n")
    file.write(f"Average Change: ${round((sum(change) / len(change)), 2)}\n")
    file.write(f"Greatest Increase in Profits: {months[change.index(max(change))+1]} ${max(change)}\n")
    file.write(f"Greatest Decrease in Profits: {months[change.index(min(change))+1]} ${min(change)}\n")
    file.close()



