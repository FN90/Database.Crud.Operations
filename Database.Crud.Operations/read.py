
import db_connection as dbConn

class Read:
    def read_data(self):   
        # Get the sql connection
        connection = dbConn.getConnection()
        cursor = connection.cursor()

        # Execute the sql query
        cursor.execute('Select * from [Python.Crud.Operations].[dbo].Product')

        # Print the data
        for row in cursor:
            print('row = %r' % (row,))