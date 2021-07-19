# from _typeshed import Self
from os import error, truncate
import sqlite3
from sqlite3.dbapi2 import Connection, Cursor, Error
import constants
import uuid
import secrets


class Content:
    def __init__(self, db_connection):
        try:
            self.db_connection = db_connection
            self.db_cursor = self.db_connection.cursor()
            self.initialise_Content()
        except Error as e:
            print(e)

    def initialise_Content(self):
        try:
            self.db_cursor.execute(constants.CREATE_TABLE_CONTENT)
            self.db_cursor.execute(constants.CREATE_TABLE_POST)
            self.db_cursor.execute(constants.CREATE_TABLE_COMMENT)
            self.db_connection.commit()
            
        except Error as e:
            print(e)
    # noc = number of comment & nol = number of likes
    def content_insert(self, content_date, content_time, content_nol, content_noc, user_uuid):
        content_id = str(uuid.uuid4().hex)
        values_tuple = (content_id, content_date, content_time, content_nol, content_noc, user_uuid)

        try:
            self.db_cursor.execute(constants.INSERT_RECORD_CONTENT, values_tuple)
            self.db_connection.commit()
            return True
        except Error as e:
            print(e)
            return False

    def post_insert(self, post_content, post_isFeatured, content_id):
        check_id = self.check_content_id(content_id)
        if not check_id:          
            return False

        values_tuple = (post_content, post_isFeatured, content_id)
        try:
            self.db_cursor.execute(constants.INSERT_RECORD_POST, values_tuple)
            self.db_connection.commit()
            return True
        except Error as e:
            print(e)
            return False

    def comment_insert(self, comment_content, comment_reply_id, content_id):

        check_id = self.check_content_id(content_id)
        check_reply_id = self.check_id_in_content_table(comment_reply_id)
        if not(check_id and check_reply_id):
            return False

        values_tuple = (comment_content, comment_reply_id, content_id)
        try:
            self.db_cursor.execute(constants.INSERT_RECORD_COMMENT, values_tuple)
            self.db_connection.commit()
            return True
        except Error as e:
            print(e)
            return False

    def check_id_in_content_table(self, content_id):
        selected_content = self.db_cursor.execute(constants.SELECT_RECORD_CONTENT, (content_id, ))
        selected_content = selected_content.fetchall()
        if len(selected_content) == 0:
            print('this content id does not exits.')
            return False
        return True

    def check_content_id(self, content_id):
        if not(self.check_id_in_content_table(content_id)):
            return False
        
        selected_post = self.db_cursor.execute(constants.SELECT_RECORD_POST, (content_id, ))
        selected_post = selected_post.fetchall()
        if len(selected_post) > 0:
            print('this content id is used before.')
            return False

        selected_comment = self.db_cursor.execute(constants.SELECT_RECORD_POST, (content_id, ))
        selected_comment = selected_comment.fetchall()
        if len(selected_comment) > 0:
            print('this content id is used before.')
            return False
        
        return True


class User:

    def __init__(self, db_connection):
        try:
            self.db_connection = db_connection
            self.db_cursor = self.db_connection.cursor()
            self.initialise_User()
            self.db_connection.commit()

        except Error as e:
            print(e)

    #table creation
    def initialise_User(self):
        try:
            self.db_cursor.execute(constants.CREATE_TABLE_USER)
            self.db_cursor.execute(constants.CREATE_TABLE_PROFILE)
            self.db_cursor.execute(constants.CREATE_TABLE_CONNECTIONS)

            self.db_connection.commit()
        except Error as e:
            print(e)


    def user_insert(self, insert_table_values):
        try:
            self.db_cursor.execute(constants.INSERT_RECORD_USER, insert_table_values)
            self.db_connection.commit()
            return True
        except Error as e:
            print(e)
            return False


    def user_delete(self, user_uuid, password):
        rv = self.user_select(user_uuid, password)
        if rv.__len__() == 0:
            return (False, 'NO SUCH RECORD FOUND!')

        try:
            self.db_cursor.execute(constants.DELETE_RECORD_PROFILE, (user_uuid, ))
            self.db_connection.commit()
        except Error as e:
            print(e)
        try:
            self.db_cursor.execute(constants.DELETE_RECORD_USER, (user_uuid, password))
            self.db_connection.commit()
        except Error as e:
            print(e)

        rv = self.user_select(user_uuid, password)
        if rv.__len__() == 0:
            return (True, 'record was deleted successfully')
        else:
            return (False, 'we had a problem deleting your record, Try again!')
    

    def user_select(self, user_uuid, password): 
        try:
            user = self.db_cursor.execute(constants.SELECT_RECORD_USER, (user_uuid, password))                                 
            # return(self.db_cursor.fetchall())
            user = user.fetchall()
            user_dict = {
                "user_uuid": user[0][0],
                "user_email": user[0][1],
                "user_password": user[0][2],
                "user_token": user[0][3],
            }
            return user_dict
        except Error as e:
            print(e)
            return None


    def user_update(self, user_uuid, user_email=None, user_password=None, user_token=None):
        # self.cursor_1.execute(constants.UPDATE_RECORD_USER, (updated_values_with_fileds, user_email))
        updated_values_with_fileds = ''
        if user_email != None:
            updated_values_with_fileds = updated_values_with_fileds + f'user_email = \'{user_email}\','
        if user_password != None:
            updated_values_with_fileds = updated_values_with_fileds + f'user_password = \'{user_password}\','
        if user_token != None:
            updated_values_with_fileds = updated_values_with_fileds + f'user_token = \'{user_token}\''

        #to remoev the last probbable ','
        u_len = len(updated_values_with_fileds)
        if updated_values_with_fileds[-1] == ',':
            updated_values_with_fileds = updated_values_with_fileds[0:u_len-1]

        try:
            self.db_cursor.execute(f'UPDATE user SET {updated_values_with_fileds} WHERE user_uuid = \'{user_uuid}\'')
            self.db_connection.commit()
            return (True)
        except Error as e:
            return (False)


    def user_signUp(self, user_email, user_password):
        user_uuid = str(uuid.uuid4())
        user_token = self.tokenGenarator()

        user_values = (user_uuid, user_email, user_password, user_token)
        signup_flag = self.user_insert(user_values)

        if signup_flag:
            return (True, user_token)
        else:
            return (False, None)
        

    def user_login(self, user_email, user_password):
        selectedUser = self.db_cursor.execute(constants.SELECT_RECORD_LOGIN_USER, (user_email, user_password))
        selectedUser = selectedUser.fetchall()
        
        if len(selectedUser) > 0:
            user_token = self.tokenGenarator()
            self.user_update(selectedUser[0][0], user_token=user_token)
            # print(user_email, f"user_token = \'{user_token}\'")
            return (True, user_token)
        else:
            return (False, None)

    def tokenGenarator(self):
        return secrets.token_urlsafe()


    
    #PROFILE METHODS
    def profile_insert(self, insert_table_values):
        try:
            self.db_cursor.execute(constants.INSERT_RECORD_PROFILE, insert_table_values)
            self.db_connection.commit()
            return True
        except Error as e:
            print(e)
            # return (False, 'had problem adding your account! try again.')
            return False
        
    def profile_select(self, user_uuid): 
        profile = self.db_cursor.execute(constants.SELECT_RECORD_PROFILE, (user_uuid,))
        profile = profile.fetchall()
        profile_dict = {
            "profile_first_name": profile[0][0],
            "profile_last_name": profile[0][1],
            "profile_headline": profile[0][2],
            "profile_country": profile[0][3],
            "profile_birthday": profile[0][4],
            "profile_address": profile[0][5],
            "profile_about": profile[0][6],
            "profile_number_of_connections": profile[0][7],
            
        }
        return profile_dict


    def profile_update(self, user_uuid, profile_first_name=None, profile_last_name=None, profile_headline=None, profile_country=None, profile_birthday=None, profile_address=None, profile_about=None, profile_number_of_connections=None):
        # self.cursor_1.execute(constants.UPDATE_RECORD_USER, (updated_values_with_fileds, user_email))
        updated_values_with_fileds = ''
        
        if profile_first_name != None:
            updated_values_with_fileds = updated_values_with_fileds + f'profile_first_name = \'{profile_first_name}\','
        if profile_last_name != None:
            updated_values_with_fileds = updated_values_with_fileds + f'profile_last_name = \'{profile_last_name}\','
        if profile_headline != None:
            updated_values_with_fileds = updated_values_with_fileds + f'profile_headline = \'{profile_headline}\','
        if profile_country != None:
            updated_values_with_fileds = updated_values_with_fileds + f'profile_country = \'{profile_country}\','
        if profile_birthday != None:
            updated_values_with_fileds = updated_values_with_fileds + f'profile_birthday = \'{profile_birthday}\','
        if profile_address != None:
            updated_values_with_fileds = updated_values_with_fileds + f'profile_address = \'{profile_address}\','
        if profile_about != None:
            updated_values_with_fileds = updated_values_with_fileds + f'profile_about = \'{profile_about}\','
        if profile_number_of_connections != None:
            updated_values_with_fileds = updated_values_with_fileds + f'profile_number_of_connections = {profile_number_of_connections}'
        
        #to remoev the last probbable ','
        u_len = len(updated_values_with_fileds)
        if updated_values_with_fileds[-1] == ',':
            updated_values_with_fileds = updated_values_with_fileds[0:u_len-1]

        try:
            self.db_cursor.execute(f'UPDATE profile SET {updated_values_with_fileds} WHERE user_uuid = \'{user_uuid}\'')
            self.db_connection.commit()
            return (True)
        except Error as e:
            return (False)



    #CONNECTION METHODS
    def connection_numberOfConnections(self, user_uuid):
        noc = self.db_cursor.execute(constants.SELECT_NOC_CONNECTIONS, (user_uuid, user_uuid))
        return noc.fetchall()[0][0]







if __name__ == '__main__':
    try:
        db_connection = sqlite3.connect(constants.DB_NAME)
        user = User(db_connection)
        content = Content(db_connection)
        # a = user.user_signUp("mad@mail", "123")
        # a = user.user_login("mad@mail", "123")
        # a = user.user_select("0e6b6077-0928-4439-b61a-393616bbd2e6", "123456")
        # a = user.user_update(user_uuid='0e6b6077-0928-4439-b61a-393616bbd2e6', user_password='123456', user_token='wh')
        # a = user.user_delete('be49687e-be68-4f31-8feb-aac66fb2479b', '456')

        
        #profile test case
        # profile_value = ('moouod', 'shahrizi', 'ce student', 'iran', '2000/00/00', 'shiraz', 'nothing about me', 0, '0e6b6077-0928-4439-b61a-393616bbd2e6')
        # print(user.profile_insert(profile_value))
        # a = user.profile_select('0e6b6077-0928-4439-b61a-393616bbd2e6')
        # a = user.profile_update('0e6b6077-0928-4439-b61a-393616bbd2e6', profile_first_name='moouod', profile_number_of_connections=8)
        # a = db.select_profile('6c2dad19-134e-483a-ba3b-5b6262cfc9bc')
        
        #connection test cases
        # a = user.connection_numberOfConnections('5b4deaa2-b056-44fb-97f2-f40ab3af9b54')

        #content & post & comment test cases
        # (content_id, content_date, content_time, content_nol, content_noc, user_uuid)
        # a = content.content_insert('2021', '12:00', 0, 0, '5b4deaa2-b056-44fb-97f2-f40ab3af9b54')
        # a = content.post_insert('my first post', 0, 'cf66524d09c74d5b83dfe00386e29ba7')
        # a = content.comment_insert('my first comment', '0002', '0001')

        # print(a)
        
        db_connection.close()
    except Error as e:
        print(e)
