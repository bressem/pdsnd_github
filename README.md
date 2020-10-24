### Date created
Created at the 24th october 2020

BIKESHARE DATA PROJECT - my first coding project

### Description
The bikeshare data project should give an overview about the data of a biskeshare company in the citys Washington, Chicago and New York City.
First you need to run the bikeshare.py
Then you get three questions:
1. "For which city do you want to see data?"
Here are three possible answers to get to the second question: washington, chicago or new york city.
As long as you don't insert one of these given citys, it will print a "not valid answer". Just one answer is possible. The answers are not cape sensitive
2. "For which month do you want to see data?"
Here are 7 possible answers to get to the third question: 'january', 'febuary', 'march', 'april', 'may', 'june', 'all'.
As long as you don't insert one of these given answers, it will print a "not valid answer".
The month will filter the data to give just the data concerning this month. "all" won't give filter and shows all the data. Just one answer is possible.  The answers are not cape sensitive  
3. "For which day of the week do you want to see data"
In this answer you need to decide, if you want to see data for a specific day of the week (for example mondays) or for the whole week ("all")
Therefor you could answer: 'monday', 'tuesday', 'wendsday', 'thursday', 'friday', 'saturday', 'sunday', 'all'
Your answer will filter the dataset to the given day(s) of week. Just one answer is possible. The answers are not cape sensitive.
After entering the day of the week the program will provide the data for you:

- Displays statistics on the most frequent times of travel
  - by month
  - by day
  - by Hour
- Displays statistics on the most popular stations and trip
  - Most popular start stations
  - Most popular end station
  - Most Popular combination of start and End Stations
- Displays statistics on the total and average trip duration.
- Displays statistics on bikeshare users

At the end it will ask you: "Would you like to see raw data? Enter yes or no"
Here you could decide if you want to see data and it will show you 5 rows of the original data set, and ask in a loop "Would you like to see more raw data? Enter yes or no"
With yes you get 5 rows more data, with no it will end the program.  

### Files used
Files are used are the data csv-Files
- washington.csv
- chicago.csv
- new_york_city.csv

### Credits
Thank you very much to udacity and it's team for providing this course, and giving me the architecture of this program and the skills to accomplish this code.
