from appconfig import SERVERNAME, DATABASENAME, USERNAME, PASSWORD
import pymssql

def createConnection():
    try:
        print('into createConnection function...')
        connection = pymssql.connect(server=SERVERNAME, 
                               database=DATABASENAME, 
                               user=USERNAME, 
                               password=PASSWORD)
    
        print('createConnection function complete!!!')

        return connection
    
    except Exception as ex:
        print(f'!!! SQL Connection Error: {ex}')
        raise ex


def insertProfileInfo(user_id, user_type, display_name, picture_url):
    try:
        print('into insertProfileInfo function...')

        connection = createConnection()
        cursor = connection.cursor()
        insert = "Insert into LineUsers(UserID, Type, DisplayName, PictureURL) values (%s, %s, %s, %s)"
        cursor.execute(insert, (user_id, user_type, display_name, picture_url))
        connection.commit()

        print('insertProfileInfo function complete!!!')
    except Exception as ex:
        print(f'!!! insertProfileInfo function error: {ex}')
        connection.rollback()

    finally:
        connection.close()



def updateLocked(user_locked, user_id):
    try:
        print('into followUpdateLocked function...')

        connection = createConnection()
        cursor = connection.cursor()
        update = "Update LineUsers set Locked = %s where UserID = %s"
        cursor.execute(update, (user_locked, user_id))
        connection.commit()

        print('followUpdateLocked function complete!!!')
    except Exception as ex:
        print(f'!!! followUpdateLocked function error: {ex}')
        connection.rollback()

    finally:
        connection.close()