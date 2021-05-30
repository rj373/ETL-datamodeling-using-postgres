# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS song"
artist_table_drop = "DROP TABLE IF EXISTS artist"
time_table_drop = "DROP TABLE IF EXISTS time_table"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplay (songplay_id serial primary key, start_time varchar not null,
            user_id varchar not null, level text, song_id text, artist_id text, session_id int, location text, user_agent text)""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (user_id varchar primary key, first_name text,last_name text, gender char, level text)""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS song (song_id varchar primary key, title varchar, artist_id text, year int, duration float)""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artist (artist_id text primary key, artist_name text, location text, latitude float, longitude float)""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time_table (start_time timestamp not null, hour int, day int, week int, month int, year int, weekday int)""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplay (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
                        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)""")

user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level)
                        VALUES(%s,%s,%s,%s,%s) ON CONFLICT (user_id) DO UPDATE SET level = excluded.level""")

song_table_insert = ("""INSERT INTO song (song_id, title, artist_id, year, duration)
                        VALUES(%s,%s,%s,%s,%s) ON CONFLICT (song_id) DO NOTHING""")

artist_table_insert = ("""INSERT INTO artist (artist_id, artist_name, location, latitude, longitude)
                        VALUES(%s,%s,%s,%s,%s) ON CONFLICT (artist_id) DO NOTHING""")


time_table_insert = ("""INSERT INTO time_table (start_time, hour, day, week, month, year, weekday)
                        VALUES(%s,%s,%s,%s,%s,%s,%s)""")

# FIND SONGS

song_select = (""" SELECT * FROM song""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]