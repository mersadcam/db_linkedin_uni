class TableColumns:

    USER_UUID = 'user_uuid'
    USER_EMAIL = 'user_email'
    USER_PASSWORD = 'user_password'
    USER_TOKEN = 'user_token'

    PROFILE_FIRST_NAME = 'profile_first_name'
    PROFILE_LAST_NAME = 'profile_last_name'
    PROFILE_HEADLINE = 'profile_headline'
    PROFILE_COUNTRY = 'profile_headline'
    PROFILE_BIRTHDAY = 'profile_headline'
    PROFILE_ADDRESS = 'profile_headline'
    PROFILE_ABOUT = 'profile_headline'
    PROFILE_LINK = 'profile_link'
    PROFILE_USER_UUID = 'user_uuid'

    CONNECTIONS_USER1_UUID = 'user1_uuid'
    CONNECTIONS_USER2_UUID = 'user2_uuid'

    CONTENT_ID = 'content_id'
    CONTENT_DATE = 'content_date'
    CONTENT_TIME = 'content_time'
    CONTENT_USER_UUID = 'user_uuid'
    
    POST_CONTENT = 'post_content'
    POST_IS_FEATURED = 'post_isFeatured'
    POST_CONTENT_ID = 'content_id'

    COMMENT_CONTENT = 'comment_content'
    COMMENT_REPLY_ID = 'comment_reply_id'
    COMMENT_CONTENT_ID = 'content_id'

    LIKE_CONTENT_ID = 'content_id'
    LIKE_USER_UUID = 'user_uuid'

    SKILL_SKILL_NAME = 'skill_name'
    SKILL_SKILL_ID = 'skill_id'



DB_NAME = 'LinkeInDB.db'

EMAIL_EXISTANCE_ERROR = 'this email is used before!'
EMAIL_FORMAT_ERROR = 'invalid email!'
# to enable foreign keys
ENABLE_FOREIGN_KEY = 'PRAGMA foreign_keys = ON;'
USER_FIELDS = ('user_uuid', 'user_email', 'user_password', 'user_token')
#user talbe constants
CREATE_TABLE_USER = """CREATE TABLE IF NOT EXISTS user(
                        user_uuid text PRIMARY KEY,
                        user_email text NOT NULL UNIQUE, 
                        user_password text NOT NULL,
                        user_token text UNIQUE
)"""
INSERT_RECORD_USER = 'INSERT INTO user(user_uuid, user_email, user_password, user_token) VALUES(?, ?, ?, ?)'
DELETE_RECORD_USER = 'DELETE FROM user WHERE user_uuid = (?)'
SELECT_RECORD_USER = 'SELECT * FROM user WHERE  user_uuid = (?)'
SELECT_RECORD_BY_TOKEN_USER = 'SELECT user_uuid FROM user WHERE user_token = (?)'
SELECT_RECORD_LOGIN_USER = 'SELECT * FROM user WHERE  user_email = (?) AND user_password = (?)'
UPDATE_CLEAR_TOKEN_USER = 'UPDATE user SET user_token = "" WHERE user_uuid = (?)'
# UPDATE_RECORD_USER = 'UPDATE user SET user_password = (?) WHERE user_email = (?)'
# UPDATE_RECORD_USER2 = 'UPDATE user SET (?) WHERE user_email = (?)'




#**************************
# profile table constants
PROFILE_FIELDS = ('profile_first_name', 'profile_last_name', 'profile_headline', 'profile_country', 'profile_birthday', 
                    'profile_address', 'profile_about', 'profile_number_of_connections', 'user_uuid')
                    
CREATE_TABLE_PROFILE = """CREATE TABLE IF NOT EXISTS profile(
                        profile_first_name text,
                        profile_last_name text, 
                        profile_headline text,
                        profile_country text,
                        profile_birthday text,
                        profile_address text,
                        profile_about text,
                        profile_link text,
                        user_uuid text NOT NULL UNIQUE,
                        FOREIGN KEY (user_uuid) REFERENCES user (user_uuid)
)"""
INSERT_RECORD_PROFILE = """INSERT INTO profile(profile_first_name, profile_last_name, profile_headline,
                                        profile_country, profile_birthday, profile_address, profile_about,
                                        profile_link, user_uuid) 
                                        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)"""
SELECT_RECORD_PROFILE = 'SELECT * FROM profile WHERE user_uuid = (?)'
DELETE_RECORD_PROFILE = 'DELETE FROM profile WHERE user_uuid = (?)'
SELECT_RECORD_SEARCH_PROFILE = """SELECT user_uuid, profile_first_name, profile_last_name FROM profile WHERE
                                 profile_first_name LIKE (?) OR profile.profile_last_name LIKE (?) LIMIT 5"""

#**************************
#connection table constants
CREATE_TABLE_CONNECTIONS = """CREATE TABLE IF NOT EXISTS connections(
                        user1_uuid text NOT NULL,
                        user2_uuid text NOT NULL,
                        FOREIGN KEY (user1_uuid) REFERENCES user (user_uuid),
                        FOREIGN KEY (user2_uuid) REFERENCES user (user_uuid)
                        
)"""

SELECT_NOC_CONNECTIONS = 'SELECT COUNT(*) FROM connections WHERE user1_uuid = (?) OR user2_uuid = (?)'

SELECT_UUID1_CONNECTIONS = 'SELECT user2_uuid FROM connections WHERE user1_uuid = (?)'
SELECT_UUID2_CONNECTIONS = 'SELECT user1_uuid FROM connections WHERE user2_uuid = (?)'



#**************************
# profile table constants
#SHOULD WE ADD CONTENT TEXT OR NOT?
CREATE_TABLE_CONTENT = """CREATE TABLE IF NOT EXISTS content(
                        content_id text PRIMARY KEY,
                        content_date_time text,
                        user_uuid text NOT NULL,
                        FOREIGN KEY (user_uuid) REFERENCES user (user_uuid)
)"""

CREATE_TABLE_POST = """CREATE TABLE IF NOT EXISTS post(
                        post_content text NOT NULL,
                        post_isFeatured integer NOT NULL,                    
                        content_id text NOT NULL UNIQUE,
                        FOREIGN KEY (content_id) REFERENCES content (content_id)
)"""

#comment_reply_id is the id of the content which this comment is refering to
#comment_id belongs to this comment
CREATE_TABLE_COMMENT = """CREATE TABLE IF NOT EXISTS comment(
                        comment_content text NOT NULL,
                        comment_reply_id text NOT NULL,
                        content_id text NOT NULL UNIQUE,
                        FOREIGN KEY (content_id) REFERENCES content (content_id),
                        FOREIGN KEY (comment_reply_id) REFERENCES content (content_id)
)"""

INSERT_RECORD_CONTENT = """INSERT INTO content (content_id, content_date_time, user_uuid) Values(?, ?, ?)"""

INSERT_RECORD_POST = """INSERT INTO post(post_content, post_isFeatured, content_id) VALUES(?, ?, ?)"""
INSERT_RECORD_COMMENT = """INSERT INTO comment(comment_content, comment_reply_id, content_id) VALUES(?, ?, ?)"""

SELECT_RECORD_CONTENT = """SELECT * FROM content WHERE content_id = (?)"""
SELECT_RECORD_POST = """SELECT * FROM post WHERE content_id = (?)"""
SELECT_ALL_RECORD_POST = """SELECT * FROM post WHERE content_id IN (SELECT content_id FROM content WHERE user_uuid = (?))"""
SELECT_RECORD_COMMENT = """SELECT * FROM comment WHERE content_id = (?)"""
SELECT_ALL_COMMENT = """SELECT * FROM comment WHERE comment_reply_id = (?)"""
SELECT_NUMBER_OF_COMMENTSS_COMMENT = 'SELECT COUNT(*) FROM comment WHERE comment_reply_id = (?)'

SELECT_ALL_USER_CONNECTIONS_POSTS = """SELECT * FROM post WHERE content_id IN 
                            (SELECT content_id FROM content WHERE user_uuid IN 
                            (SELECT user2_uuid FROM connections WHERE user1_uuid = (?)) OR
                            user_uuid IN (SELECT user1_uuid FROM connections WHERE user2_uuid = (?)) ORDER BY content_date_time)"""

DELETE_RECORD_CONTENT = 'DELETE FROM content WHERE content_id = (?)'
DELETE_RECORD_POST = 'DELETE FROM post WHERE content_id = (?)'
DELETE_RECORD_COMMENT = 'DELETE FROM comment WHERE content_id = (?)'


#LIKE TABLE
CREATE_TABLE_LIKE = """CREATE TABLE IF NOT EXISTS like(                    
                        content_id text NOT NULL,
                        user_uuid text NOT NULL,
                        FOREIGN KEY (content_id) REFERENCES content (content_id),
                        FOREIGN KEY (user_uuid) REFERENCES user (user_uuid)
)"""
# PRIMARY KEY (user_uuid, content_id)

INSERT_RECORD_LIKE = """INSERT INTO like(content_id, user_uuid) VALUES(?, ?)"""
DELETE_RECORD_LIKE = 'DELETE FROM like WHERE content_id = (?) AND user_uuid = (?)'
SELECT_NUMBER_OF_LIKES_LIKE = 'SELECT COUNT(*) FROM like WHERE content_id = (?)'

CREATE_TABLE_SKILL = """CREATE TABLE IF NOT EXISTS skill(
                        skill_name text NOT NULL,
                        skill_id text PRIMARY KEY
)"""
SELECT_ALL_SKILLS = 'SELECT * FROM skill'
INSERT_SKILL = 'INSERT INTO skill(skill_name, skill_id) VALUES(?, ?)'

CREATE_TABLE_USER_SKILL = """CREATE TABLE IF NOT EXISTS user_skill(
                              skill_id text NOT NULL,
                              user_uuid text NOT NULL,
                              FOREIGN KEY (skill_id) REFERENCES skill (skill_id),
                              FOREIGN KEY (user_uuid) REFERENCES user (user_uuid)
)"""

INSERT_USER_SKILL = 'INSERT INTO user_skill(skill_id, user_uuid) VALUES(?, ?)'
SELECT_ALL_USER_SKILLS = 'SELECT * FROM skill WHERE skill_id IN (SELECT skill_id FROM user_skill WHERE user_uuid = (?))'
DELETE_USER_SKILL = 'DELETE FROM user_skill WHERE skill_id = (?) AND user_uuid = (?)'

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

