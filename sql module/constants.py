DB_NAME = 'LinkeInDB.db'


# create_table_name = ''
# create_table_fields = ''
# create_table = f'CREATE TABLE IF NOT EXISTS {create_table_name}({create_table_fields})'

# to enable foreign keys
ENABLE_FOREIGN_KEY = 'PRAGMA foreign_keys = ON;'

#user talbe constants
CREATE_TABLE_USER = """CREATE TABLE IF NOT EXISTS user(
                        user_uuid text PRIMARY KEY,
                        user_email text NOT NULL UNIQUE, 
                        user_password text NOT NULL,
                        user_token text UNIQUE
)"""
INSERT_RECORD_USER = 'INSERT INTO user(user_uuid, user_email, user_password, user_token) Values(?, ?, ?, ?)'
DELETE_RECORD_USER = 'DELETE FROM user WHERE user_email = (?) AND user_password = (?)'
SELECT_RECORD_USER = 'SELECT * FROM user WHERE  user_email = (?) AND user_password = (?)'
UPDATE_CLEAR_TOKEN_USER = 'UPDATE user SET user_token = '' WHERE user_email = (?)'
# UPDATE_RECORD_USER = 'UPDATE user SET user_password = (?) WHERE user_email = (?)'
# UPDATE_RECORD_USER2 = 'UPDATE user SET (?) WHERE user_email = (?)'

#**************************
# profile table constants
CREATE_TABLE_PROFILE = """CREATE TABLE IF NOT EXISTS profile(
                        profile_first_name text,
                        profile_last_name text, 
                        profile_headline text,
                        profile_country text,
                        profile_birthday text,
                        profile_address text,
                        profile_about text,
                        profile_number_of_connections integer,
                        user_email text NOT NULL UNIQUE,
                        user_uuid text NOT NULL UNIQUE,
                        FOREIGN KEY (user_uuid) REFERENCES user (user_uuid)
                        FOREIGN KEY (user_email) REFERENCES user (user_email)
)"""
INSERT_RECORD_PROFILE = """INSERT INTO profile(profile_first_name, profile_last_name, profile_headline,
                                        profile_country, profile_birthday, profile_address, profile_about,
                                        profile_number_of_connections, user_email, user_uuid) 
                                        Values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
SELECT_RECORD_PROFILE = 'SELECT * FROM profile WHERE  user_email = (?) OR user_uuid = (?)'
DELETE_RECORD_PROFILE = 'DELETE FROM profile WHERE user_email = (?)' # OR user_uuid = (?) => probbably would be needed


#**************************
#connection table constants
CREATE_TABLE_CONNECTIONS = """CREATE TABLE IF NOT EXISTS connections(
                        user1_email text NOT NULL UNIQUE,
                        user2_email text NOT NULL UNIQUE,
                        FOREIGN KEY (user1_email) REFERENCES user (user_email),
                        FOREIGN KEY (user2_email) REFERENCES user (user_email)
                        
)"""

SELECT_NOC_CONNECTIONS = 'SELECT COUNT(*) FROM connections WHERE user1_email = (?) OR user2_email = (?)'
# create_table_profile = """CREATE TABLE IF NOT EXISTS profile(
#                         profile_id integer PRIMARY KEY,
#                         FOREIGN KEY (user_id) REFERENCES user (user_id)
# )"""

# create_table_connections = """CREATE TABLE IF NOT EXISTS connections(
#                         connection_id integer PRIMARY KEY,
#                         FOREIGN KEY (user1_id) REFERENCES user (user_id),
#                         FOREIGN KEY (user2_id) REFERENCES user (user_id)
# )"""

# insert_table_name = ''
# insert_table_fields = ''
# insert_table_values = ''
# insert_table = f'INSERT INTO {insert_table_name} ({insert_table_fields}) VALUES({insert_table_values})'
# insert_table = f'INSERT INTO user ()'
