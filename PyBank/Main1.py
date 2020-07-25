import os 
import csv

bankdata = os.path.join("..", "Resources", "bank_data.csv")

total_months=[]
net_total_profit = []
change_in_profit = []


with open(bankdata) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")

    csvheader = next(csvreader)
    #loop through rows to append total months and net_total_profit to list
    for row in csvreader:
        
        total_months.append(row[0])
        net_total_profit.append(int(row[1]))
    #loop through net_total_profit loss to compute the difference between two months and append to monthly_changes
    for profit in range(len(net_total_profit)-1):
            change_in_profit.append(net_total_profit[profit+1]-net_total_profit[profit])

    #average of change_in_profit 
    len_total_months = len(total_months)
    total_profit = sum(net_total_profit)
    average = round(sum(change_in_profit)/len(change_in_profit), 2)

    #calculating greatest increase and decrease of changes
    change_max = max(change_in_profit)
    change_min = min(change_in_profit)

    month_max = change_in_profit.index(max(change_in_profit))+1
    month_min = change_in_profit.index(min(change_in_profit))+1


print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {len_total_months}")
print(f"Total: {total_profit}")
print(f"Average Change: {average}")
print(f"Greatest Increase in Profit: {total_months[month_max]} (${str(change_max)})")
print(f"Greatest Decrease in Profit: {total_months[month_min]} (${str(change_min)})")

        
financial_analysis = open('financial_analysis.txt', "w")
financial_analysis.write("Financial Analysis\n")
financial_analysis.write("---------------------------\n")
financial_analysis.write(f"Total Months: {len_total_months}\n")
financial_analysis.write(f"Total: {total_profit}\n")
financial_analysis.write(f"Average Change: {average}\n")
financial_analysis.write(f"Greatest Increase in Profit: {total_months[month_max]} (${str(change_max)})\n")
financial_analysis.write(f"Greatest Decrease in Profit: {total_months[month_min]} (${str(change_min)})\n")
financial_analysis.close()        
        