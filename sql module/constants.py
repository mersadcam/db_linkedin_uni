DB_NAME = 'LinkeInDB.db'


# create_table_name = ''
# create_table_fields = ''
# create_table = f'CREATE TABLE IF NOT EXISTS {create_table_name}({create_table_fields})'

CREATE_TABLE_USER = """CREATE TABLE IF NOT EXISTS user(
                        user_uuid text PRIMARY KEY,
                        user_email text NOT NULL UNIQUE, 
                        user_password text NOT NULL,
                        user_token text UNIQUE
)"""
INSERT_RECORD_USER = 'INSERT INTO user(user_uuid, user_email, user_password, user_token) Values(?, ?, ?, ?)'
DELETE_RECORD_USER = 'DELETE FROM user WHERE user_email = (?) AND user_password = (?)'
SELECT_RECORD_USER = 'SELECT * FROM user WHERE  user_email = (?) AND user_password = (?)'
UPDATE_RECORD_USER = 'UPDATE user SET user_password = (?) WHERE user_email = (?)'
UPDATE_RECORD_USER2 = 'UPDATE user SET (?) WHERE user_email = (?)'


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

