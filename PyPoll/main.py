import os
import csv

csvpath = os.path.join("..", "Resources", "election_data.csv")

total_votes = 0
candidates = {}
percent_votes_candidates = {}
total_votes_candidates = 0
winner_name = None


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    
    for row in csvreader:
        total_votes = total_votes + 1
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1
    #calculating individual candidate percentages
    for key, value in candidates.items():
        percent_votes_candidates[key] = (value/total_votes)*100
    #calculating winner based on greatest votes
    for key in candidates.keys():
        if candidates[key] > total_votes_candidates:
            winner_name = key
            total_votes_candidates = candidates[key]
    

    print("---------------------------")
    print("Election Results")
    print("---------------------------")
    print(f"Total Votes: {total_votes}")
    print("---------------------------")
    
    for key, value in candidates.items():
        print(key+":", str(round(percent_votes_candidates[key], 3))+"%", "("+str(value)+")")
    print("---------------------------")
    print(f"Winner: {winner_name}")
    print("---------------------------")

election_results = open('election_results.txt', "w")
election_results.write("---------------------------\n")
election_results.write("Election Results\n")
election_results.write("---------------------------\n")
election_results.write(f"Total Votes: {total_votes}\n")
election_results.write("---------------------------\n")
for key, value in candidates.items():
    election_results.write(key+": " + str(round(percent_votes_candidates[key], 3))+"% " + " ("+str(value)+")\n")
election_results.write("---------------------------\n")
election_results.write(f"Winner: {winner_name}\n")
election_results.write("---------------------------\n")
election_results.close()