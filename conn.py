import mysql.connector
class Conndb():

    try:
    ##---Coonect to database--##

        config = {
            'user': 'shivam',
            'password': 'shivam',
            'host': 'localhost',
            'database': 'vaccine',
            # 'raise_on_warnings': True
        }
        conn = mysql.connector.connect(**config)
        curs = conn.cursor()

    except:
        conn.close()
        print("COnnection Failed Closing conn")