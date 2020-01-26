import csv
#what we need


#read in CSV

with open("Resources/election_results.csv", "r") as data:

    #rows = data.readlines()
    rows = csv.reader(data)

    headers = next(rows)
    print(headers)
#print(len(rows))
    total_votes = 0

    candidate_votes = {}

    for row in rows:
        total_votes += 1
        row_data = row
        #print(row_data[2])
        candidate_name = row_data[2]

        if candidate_name not in candidate_votes.keys():
            candidate_votes.update({ candidate_name : { "total":0 } })
        
        candidate_votes[candidate_name]["total"] += 1

        district = row_data[1]

        if district not in candidate_votes[candidate_name].keys():
            candidate_votes[candidate_name].update({ district: 1 })
        else:
            candidate_votes[candidate_name][district] += 1
    print(candidate_votes)

with open("Analysis/election_analysis.txt", "w") as output_file:

    for candidate in candidate_votes:
        output_file.write(f"Candidate: {candidate}, total votes: {candidate_votes[candidate]['total']}")
#1.  total num of votes cast

#2.  list of candidates who recieved votes

#3.  percentage of votes candidates won

#4.  total number of votes each candidate won

#5  the winner

