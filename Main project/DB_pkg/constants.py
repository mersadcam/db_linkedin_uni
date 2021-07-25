class TableColumns:

    USER_UUID = 'user_uuid'
    USER_EMAIL = 'user_email'
    USER_PASSWORD = 'user_password'
    USER_TOKEN = 'user_token'

    PROFILE_FIRST_NAME = 'profile_first_name'
    PROFILE_LAST_NAME = 'profile_last_name'
    PROFILE_HEADLINE = 'profile_headline'
    PROFILE_COUNTRY = 'profile_country'
    PROFILE_BIRTHDAY = 'profile_birthday'
    PROFILE_ADDRESS = 'profile_address'
    PROFILE_ABOUT = 'profile_about'
    PROFILE_LINK = 'profile_link'
    PROFILE_USER_UUID = 'user_uuid'

    CONNECTIONS_USER1_UUID = 'user1_uuid'
    CONNECTIONS_USER2_UUID = 'user2_uuid'

    CONTENT_ID = 'content_id'
    CONTENT_DATE = 'content_date'
    CONTENT_TIME = 'content_time'
    CONTENT_DATE_TIME = 'content_date_time'
    CONTENT_USER_UUID = 'user_uuid'
    CONTENT_NUMBER_OF_LIKES = 'content_number_of_likes'
    CONTENT_NUMBER_OF_COMMENTS = 'content_number_of_comments'
    CONTENT_OWNER = 'content_owner'
    CONTENT_OWNER_FNAME = 'content_owner_first_name'
    CONTENT_OWNER_LNAME = 'content_owner_last_name'
    
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

    ENV_ENV_NAME = 'env_name'
    ENV_ENV_ID = 'env_id'

    BACKGROUND_ENV = 'bg_env'
    BACKGROUND_ENV_ID = 'env_id'
    BACKGROUND_USER_UUID = 'user_uuid'
    BACKGROUND_DESCRIPTION = 'bg_description'
    BACKGROUND_TITLE = 'bg_title'
    BACKGROUND_START_DATE = 'bg_start_date'
    BACKGROUND_END_DATE = 'bg_end_date'
    BACKGROUND_BG_ID = 'bg_id'

    RECOM_ID = 'recom_id'
    RECOM_WRITER_UUID = 'recom_writer_uuid'
    RECOM_RECIEVER_UUID = 'recom_reciever_uuid'
    RECOM_TEXT = 'recom_text'
    RECOM_WRITER = 'recom_writer'
    RECOM_WRITER_FNAME = 'recom_writer_first_name'
    RECOM_WRITER_LNAME = 'recom_writer_last_name'

    ACCOMP_ID = 'accomp_id'
    ACCOMP_TITLE = 'accomp_title'
    ACCOMP_TEXT = 'accomp_text'
    ACCOMP_DATE = 'accomp_date'
    ACCOMP_LINK = 'accomp_link'

    USER_ACCOMP_ACCOMP_ID = 'accomp_id'
    USER_ACCOMP_USER_UUID = 'user_uuid'

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
                                 profile_first_name LIKE (?) OR profile.profile_last_name LIKE (?)  LIMIT 5"""

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
INSERT_RECORD_CONNECTIONS = 'INSERT INTO connections(user1_uuid, user2_uuid) VALUES(?, ?)'
DELETE_RECORD_CONNECTIONS = 'DELETE FROM connections WHERE user1_uuid = (?) AND user2_uuid = (?)'
# SELECT_UUID1_NETWORK = f'SELECT DISTINCT user2_uuid FROM connections WHERE user1_uuid IN({SELECT_UUID1_CONNECTIONS}) OR user1_uuid IN({SELECT_UUID2_CONNECTIONS})'
# SELECT_UUID2_NETWORK = f'SELECT DISTINCT user1_uuid FROM connections WHERE user2_uuid IN({SELECT_UUID1_CONNECTIONS}) OR user2_uuid IN({SELECT_UUID2_CONNECTIONS})'

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

SELECT_USER_UUID_BY_CONTENT = 'SELECT user_uuid FROM content WHERE content_id = (?)'

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

#SKILL
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

#BACKGROUND
CREATE_TABLE_ENV = """CREATE TABLE IF NOT EXISTS env(
                        env_name text,
                        env_id text PRIMARY KEY                        
)"""
SELECT_ALL_ENV = 'SELECT * FROM  env'
SELECT_ENV = 'SELECT * FROM  env WHERE env_id = (?)'
INSERT_ENV = 'INSERT INTO env(env_name, env_id) VALUES(?, ?)'


CREATE_TABLE_BACKGROUND = """CREATE TABLE IF NOT EXISTS background( 
                              bg_id text PRIMARY KEY,
                              env_id text NOT NULL,
                              user_uuid text NOT NULL,
                              bg_title text,
                              bg_description text,
                              bg_start_date text NOT NULL,
                              bg_end_date text,
                              FOREIGN KEY (env_id) REFERENCES env (env_id),
                              FOREIGN KEY (user_uuid) REFERENCES user (user_uuid)
)"""

INSERT_BACKGROUND = 'INSERT INTO background(bg_id, env_id, user_uuid, bg_title, bg_description, bg_start_date, bg_end_date) VALUES(?, ?, ?, ?, ?, ?, ?)'
SELECT_ALL_BACKGROUND = 'SELECT * FROM  background WHERE user_uuid = (?)'
DELETE_BACKGROUND = 'DELETE FROM background WHERE bg_id = (?)'

#recommendation
CREATE_TABLE_RECOM = """CREATE TABLE IF NOT EXISTS recom(
                              recom_id text PRIMARY KEY,
                              recom_writer_uuid text NOT NULL,
                              recom_reciever_uuid text NOT NULL,
                              recom_text text,
                              FOREIGN KEY (recom_writer_uuid) REFERENCES user (user_uuid),
                              FOREIGN KEY (recom_reciever_uuid) REFERENCES user (user_uuid)
)"""
INSERT_RECOM = 'INSERT INTO recom(recom_id, recom_writer_uuid, recom_reciever_uuid, recom_text) VALUES(?, ?, ?, ?)'
DELETE_RECOM = 'DELETE FROM recom WHERE recom_id = (?)'
SELECT_RECOM = 'SELECT * FROM  recom WHERE recom_id = (?)'
SELECT_GET_RECOM_ID = 'SELECT * FROM  recom WHERE recom_writer_uuid = (?) AND recom_reciever_uuid = (?)'
SELECT_RECIEVED_RECOM = 'SELECT * FROM  recom WHERE recom_reciever_uuid = (?)'

#accomplishment
CREATE_TABLE_ACCOMP = """CREATE TABLE IF NOT EXISTS accomp( 
                              accomp_id text PRIMARY KEY,
                              accomp_title text,
                              accomp_text text,
                              accomp_date text,
                              accomp_link text
)"""

INSERT_ACCOMP = 'INSERT INTO accomp(accomp_id, accomp_title, accomp_text, accomp_date, accomp_link) VALUES(?, ?, ?, ?, ?)'
DELETE_ACCOMP = 'DELETE FROM accomp WHERE accomp_id = (?)'
SELECT_ACCOMP = 'SELECT * FROM accomp WHERE accomp_id = (?)'


CREATE_TABLE_USER_ACCOMP = """CREATE TABLE IF NOT EXISTS user_accomp( 
                              accomp_id text NOT NULL,
                              user_uuid text NOT NULL,
                              FOREIGN KEY (accomp_id) REFERENCES accomp (accomp_id),
                              FOREIGN KEY (user_uuid) REFERENCES user (user_uuid)
)"""

INSERT_USER_ACCOMP = 'INSERT INTO user_accomp(accomp_id, user_uuid) VALUES(?, ?)'
DELETE_USER_ACCOMP = 'DELETE FROM user_accomp WHERE accomp_id = (?) AND user_uuid = (?)'

#******************************
#******************************
#no time for ui

SELECT_LIKED_POSTS_BY_USER_CONNECTIONS = 'SELECT content_id FROM like WHERE user_uuid IN (SELECT user_uuid FROM )'
