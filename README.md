# Election_Analysis

## Project Overview

 A Colorado Board of Elections employee has given me the following tasks to complete the election audit of a recent local congressional election.

 1. Calculate the total number of votes cast.
 3. Get a complete list of candidates who received votes.
 4. Get a complete list of counties that received votes.
 5. Calculate the total number of votes each candidate received.
 6. Calcualte the total number of votes each county cast.
 7. Calculate the percentage of votes each candidate won.
 8. Calculate which county had the largest percentage of votes.
 9. Determine and report the winner of the election based on popular vote.
 10. Report the county with the highest voter turnout.

 ## Resources
 - Data Source: election_results.csv
 - Software: Python 3.6.1, Visual Studio Code, 1.62.0

 ## Summary
 The analysis of the election show that:
 - There were 369,711 votes cast in the election.
 - The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
    - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
    - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.
- The counties that voted were:
    - Jefferson
    - Denver
    - Arapahoe
- The county voting results were:
    - Jefferson county had 10.5% of the votes, with 38855 voters.
    - Denver county had 82.8 of the votes, with 306055 voters.
    - Arapahoe county had 6.7% of the votes, with 24801 voters.
- The county with the largest voter tunout:
    - Denver county, which received 82.8% of the votes, a total of 306055 voters.

## Program Overview (Challenge Overview)

This is a python script that is used to summarize the findings of an election from CSV data into a readable, summary text file.  This can be refactored and applied to any kind of summary/election/talley system.  The primary code uses a combination of for-loops and conditionals to iterate through a list of election results, tallying up the iterations and storing data/results using dictionaries.  The dictionaries are then parsed to report the results of the different categories, in this case, candidates and counties.

## Potential Code Modifications (Challenge Summary)

The code could be modified in a variety of ways to change how the results are reported.  For example, rather than a full display of all candidates and the minners at the end in a text file, the code could take in user input to report results for a particular candidate or county that is being requested by the user.  Alternatively, the code could take on a validation role by checking the validity of the results, keeping an inventory of the Ballot IDs to make sure none were counted more than once.

