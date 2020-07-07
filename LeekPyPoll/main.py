# Import os module
import os

# Import module for reading CSV files
import csv

pypollcsv = os.path.join("Resources", "election_data.csv")

#creating lists
unique_candidates=[]

votes=[]



#initialize variables
count=0
#total_profit = 0
#change = 0
#profit=0
current_winner_votes = 0
current_winner_name="default"



with open(pypollcsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    

    for row in csvreader:
        #how many votes were cast
        count = count + 1
        votes.append(row[2])
        total_votes = len(votes)
        dictionary={}
        

        if (row[2]) not in unique_candidates:
            unique_candidates.append(row[2])


    
    #print(votes)
    print(f'{"There were "}{len(votes)}{" votes cast."}')
    for candidate in unique_candidates:
        count = votes.count(candidate)
        percent = round(count/total_votes, 4)
        print(f'{candidate}{" got "}{percent}{" percent of the vote "}{"("}{count}{" votes)"}')
    
        if count >= current_winner_votes:
            current_winner_votes = count
            current_winner_name = candidate
       

print(f'{"The winner is "}{current_winner_name}{"."}')

new_file = open("output.txt", "x")
f = open("output.txt", "a")
nl = '\n'
f.write(f'{"PyPoll Results"}{nl}')

f.write(f'{"There were "}{len(votes)}{" votes cast."}{nl}')
for candidate in unique_candidates:
    count = votes.count(candidate)
    percent = round(count/total_votes, 4)
    f.write(f'{candidate}{" got "}{percent}{" percent of the vote "}{"("}{count}{" votes)"}{nl}')
    
    if count >= current_winner_votes:
        current_winner_votes = count
        current_winner_name = candidate
       

f.write(f'{"The winner is "}{current_winner_name}{"."}')

f.close()
