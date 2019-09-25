
import db_connection as dbConn;

class Delete:
    def delete_data(self):
        # Get the SQL connection
        connection = dbConn.getConnection()
        # Ask the user for the Id of the product
        id = input('Enter Product Id = ')
    
        try:
           # Get record which needs to be deleted
           sql = "Select * From [Python.Crud.Operations].[dbo].Product Where Id = ?" 
           cursor = connection.cursor()
           cursor.execute(sql, [id])
           item = cursor.fetchone()
           print('Data Fetched for Id = ', id)
           print('ID\t\t Name\t\t\t Code \t\t\t Price')
           print('-------------------------------------------')       
           print(' {}\t\t {} \t\t\t{} '.format(item[0], item[1], item[2], item[3]))
           print('-------------------------------------------')
           # Get user's delete confirmation
           confirm = input('Are you sure you want to delete this record (Y/N)?')

           # Delete after confirmation
           if confirm == 'Y':
               deleteQuery = "Delete From [Python.Crud.Operations].[dbo].Product Where Id = ?"
               cursor.execute(deleteQuery,[id])
               connection.commit()
               print('Data deleted successfully!')
           else:
                print('Wrong Entry')
        except Exception as e:
            print('Something wrong, please check. Error:'+str(e))
        finally:
            connection.close()