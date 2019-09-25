
import db_connection as dbConn

class Create:
    def create_data(self):

        # Get the sql connection
        connection = dbConn.getConnection()
                
        name = input('Enter Name = ')
        code = input('Enter Code = ')
        price = input('Enter Price = ')

        try:
           query = "Insert Into [Python.Crud.Operations].[dbo].Product(Name, Code, Price) Values(?,?,?)" 
           cursor = connection.cursor()

           # Execute the sql query
           cursor.execute(query, name, code, price)

           # Commit the data
           connection.commit()
           print('Data Saved Successfully')

        except Exception as e:
             print('Something wrong, please check. Error:'+str(e))

        finally:
           # Close the connection
           connection.close()