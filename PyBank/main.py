# Dependencies
import os
import csv

# Specifiy the file to read
budget_data_path = os.path.join('C:/','Users/','Administrator/','Documents/','GitHub/','python-challenge/','PyBank/','Resources/','budget_data.csv')

# Create new lists to save the data
date=[]
profit=[]
profit_change=[]
i=1
total_profit=0

# Read data from file and store in lists
with open(budget_data_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader,None)
    
    for row in csvreader:
        date.append(row[0])
        profit.append(row[1])
        total_profit=int(row[1])+total_profit

# Calculate the profit change and store in list        
while i<=len(profit)-1:
    k=int(profit[i])-int(profit[i-1])
    profit_change.append(k)
    i=i+1

# Calculate the total month, total profit, average change, greatest increase and decrease
total_month=len(date)
total_change = sum(profit_change)  
average_change=float(total_change/len(profit_change))
greatest_increase=max(profit_change)
greatest_increase_date=date[profit_change.index(greatest_increase)+1]
greatest_decrease=min(profit_change)
greatest_decrease_date=date[profit_change.index(greatest_decrease)+1]

# Print the results to terminal        
print("Financial Analysis")
print("----------------------------")
print(f"Total Month: {len(date)}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${average_change:6.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Specify the route for output file
output_file = os.path.join('C:/','Users/','Administrator/','Documents/','GitHub/','python-challenge/','PyBank/','analysis/',"budget_data_output.csv")

# Write results to output file
with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Financial Analysis"])
    writer.writerow(["----------------------------"])
    writer.writerow([f"Total Month: {len(date)}"])
    writer.writerow([f"Total: ${total_profit}"])
    writer.writerow([f"Average Change: ${average_change:6.2f}"])
    writer.writerow([f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})"])
    writer.writerow([f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})"])