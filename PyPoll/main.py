# Import appropriate os and csv modules
import os
import csv


#Open the poll data
poll_data = os.path.join('Resources', 'PyPoll_Resources_election_data.csv')


#Instantiate the total votes count
tallied_votes = 0

	
#Create empty list of votes for tallying
votes = {}

#Open the poll data and skip the header
with open(poll_data) as election_data:
	reader = csv.reader(election_data)
	
	header = next(reader)
	



#Run through each row of the data sheet to tally the votes for each candidate
	for row in reader:
		
		if row[2] in votes: 
			votes[row[2]] +=1
		else: 
			votes[row[2]] = 1


		tallied_votes += 1
		

	

winner = ""
winner_votes = 0 


#Print the results
print("Election Results")
print("-----------------------------")
print(f"Total Votes  {tallied_votes} ")
print("-----------------------------")

#Print the percentages for each of the candidates
for vote in votes:

	if votes[vote] > winner_votes:
		winner = vote
		winner_votes = votes[vote]

	vote_ratio = (votes[vote]/tallied_votes)
	vote_percentage = "{:.3%}".format(vote_ratio)

	print(f"{vote}: {vote_percentage} % ({votes[vote]})")


#Print the winner
print(f"Winner: {winner}")
print("-----------------------------")

  #Print the Results to a text file

with open(os.path.join('analysis', "analysis.txt"), 'w') as f:
	f.write(f'Election Results\n')
	f.write(f'-----------------------------\n')
	f.write(f'Total Votes: {tallied_votes}\n')
	f.write(f'-----------------------------\n')
	for vote in votes:

		if votes[vote] > winner_votes:
			winner = vote
			winner_votes = votes[vote]

		vote_ratio = (votes[vote]/tallied_votes)
		vote_percentage = "{:.3%}".format(vote_ratio)
		f.write(f'{vote}: {vote_percentage} % ({votes[vote]})\n')
	f.write(f'winner:  {winner}\n')
	f.write(f'-----------------------------\n')
  





