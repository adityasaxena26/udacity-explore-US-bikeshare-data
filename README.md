## Explore US Bikeshare Data

This project is a part of Udacity's Data Scientist Nanodegree Program. In this project, you will make use of Python to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. You'll write code to import the data and answer interesting questions about it by computing descriptive statistics, and a script that takes in raw input to create an interactive experience in the terminal to present these statistics.


### The Datasets

In this project, you will use data provided by Motivate, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. You will compare the system usage between three large cities: Chicago, New York City, and Washington, DC.

You will need the three city dataset files:
- chicago.csv
- new_york_city.csv
- washington.csv

All three of these bikeshare datasets are uploaded in bikeshare-data folder. You may download and open up these files to do your project work on your local machine.

Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

1. Start Time (e.g., 2017-01-01 00:07:57)
2. End Time (e.g., 2017-01-01 00:20:53)
3. Trip Duration (in seconds - e.g., 776)
4. Start Station (e.g., Broadway & Barry Ave
5. End Station (e.g., Sedgwick St & North Ave)
6. User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:

- Gender
* Birth Year

### Statistics Computed

In this project, you'll write code to provide the following information:

1. Popular times of travel (i.e., occurs most often in the start time)
   - most common month
   * most common day of week
   - most common hour of day


2. Popular stations and trip
   * most common start station
   * most common end station
   * most common trip from start to end (i.e., most frequent combination of start station and end station)


3. Trip duration
   * total travel time
   - average travel time


4. User info
   * counts of each user type
   * counts of each gender (only available for NYC and Chicago)
   * earliest, most recent, most common year of birth (only available for NYC and Chicago)

### How to install the project?
   To complete this project, the following software requirements apply:

   - You should have Python 3, NumPy, and pandas installed using Anaconda

   - A text editor, like Sublime or Atom.

   - A terminal application (Terminal on Mac and Linux or Cygwin on Windows).
