create_tables.py:
The script, create_tables.py
- Creates and connects to the sparkifydb
- Returns the connection and cursor to sparkifydb
The script runs in the terminal without errors. 
The script successfully connects to the Sparkify database, drops any tables if they exist, and creates the tables.

sql_queries.py:
CREATE statements in sql_queries.py specify all columns for each of the five tables with the right data types and conditions.

etl.py:
The script, etl.py, runs in the terminal without errors. 
The script connects to the Sparkify database, extracts and processes the log_data and song_data, and loads data into the five tables.

Since this is a subset of the much larger dataset, the solution dataset will only have 1 row with values for value containing ID for both songid and artistid in the fact table. 
Those are the only 2 values that the query in the sql_queries.py will return that are not-NONE. The rest of the rows will have NONE values for those two variables.

INSERT statements are correctly written for each table, and handle existing records where appropriate. songs and artists tables are used to retrieve the correct information for the songplays INSERT.


etl.pynb:
In this first part, you'll perform ETL on the first dataset, song_data, to create the songs and artists dimensional tables.

Let's perform ETL on a single song file and load a single record into each table to start.

Use the get_files function provided above to get a list of all song JSON files in data/song_data
Select the first song in this list
Read the song file and view the data

In this part, you'll perform ETL on the second dataset, log_data, to create the time and users dimensional tables, as well as the songplays fact table.

Let's perform ETL on a single log file and load a single record into each table.

Use the get_files function provided above to get a list of all log JSON files in data/log_data
Select the first log file in this list
Read the log file and view the data