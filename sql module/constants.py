DB_NAME = 'LinkeInDB.db'


# create_table_name = ''
# create_table_fields = ''
# create_table = f'CREATE TABLE IF NOT EXISTS {create_table_name}({create_table_fields})'

CREATE_TABLE_USER = """CREATE TABLE IF NOT EXISTS user(
                        user_email text PRIM UNIQUE, 
                        user_password text NOT NULL
)"""
INSERT_TABLE_USER = 'INSERT INTO user(user_email, user_phoneNumber, user_password) Values(?, ?, ?)'
DELETE_RECORD_USER = 'DELETE FROM user WHERE (user_email = (?) OR user_phoneNumber = (?) ) AND user_password = (?)'


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

