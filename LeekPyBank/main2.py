# Import os module
import os

# Import module for reading CSV files
import csv

pybankcsv = os.path.join("Resources", "budget_data.csv")

#creating lists
profit_list=[]
monthly_change_list=[]
month=[]

#initialize variables
count=0
total_profit = 0
change = 0
profit=0


with open(pybankcsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        #how many months are in dataset
        count = count + 1
        month.append(row[0])
        profit_list.append(row[1])
        total_profit = total_profit + int(row[1])
        #print(profit_list) #profit list thus far

        if change ==0:
            profit = int(row[1])
            change = profit - change
            monthly_change_list.append(change)
            
        elif change !=0:
            profit = int(row[1])
            change = profit - change
            monthly_change_list.append(change)
            change = profit


monthly_change_list.pop(0)
average_change = (sum(monthly_change_list)/len(monthly_change_list))

print(f'{"There are "} {count}{" months in this data set."}')
print(f'{"The total profit was "}{total_profit}{" dollars."}')
print(f'{"The average month-to-month change was "}{average_change}{" dollars."}')

max_change = max(monthly_change_list)
min_change = min(monthly_change_list)
month_of_max = monthly_change_list.index(max_change) +1
month_of_min = monthly_change_list.index(min_change) +1

print(f'{"The greatest increase in profits was "} {max_change}{" dollars."}{"("}{month[month_of_max]}{")"}')
print(f'{"The greatest decrease in profits was "} {min_change}{" dollars."}{"("}{month[month_of_min]}{")"}')


            
new_file = open("output.txt", "x")
f = open("output.txt", "a")
nl = '\n'
f.write(f'{"PyBank Results"}{nl}')
f.write(f'{"There are "}{count}{" months in this data set."}{nl}')
f.write(f'{"The total profit was "}{total_profit}{" dollars."}{nl}')
f.write(f'{"The average month-to-month change was "}{average_change}{" dollars."}{nl}')
f.write(f'{"The greatest increase in profits was "} {max_change}{" dollars."}{"("}{month[month_of_max]}{")"}{nl}')
f.write(f'{"The greatest decrease in profits was "} {min_change}{" dollars."}{"("}{month[month_of_min]}{")"}{nl}')

f.close()