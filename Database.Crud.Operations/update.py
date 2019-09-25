import db_connection as dbConn;

class Update:
    def update_data(self):
        # Get the SQL connection
        connection = dbConn.getConnection()

        id = input('Enter Product Id = ')
    
        try:
           # Fetch the data which needs to be updated
           sql = "Select * From  [Python.Crud.Operations].[dbo].Product Where Id = ?" 
           cursor = connection.cursor()
           cursor.execute(sql, [id])
           item = cursor.fetchone()
           print('Data Fetched for Id = ', id)
           print('ID\t\t Name\t\t\t Code \t\t\t Price')
           print('-------------------------------------------')       
           print(' {}\t\t {} \t\t\t{} '.format(item[0], item[1], item[2], item[3]))
           print('-------------------------------------------')
           print('Enter New Data To Update Product Record ')

           name = input('Enter New Name = ')
           code = input('Enter New Code = ')
           price = input('Enter New Price = ')
           query = "Update [Python.Crud.Operations].[dbo].Product Set Name = ?, Code = ?, Price = ? Where Id =?" 
       
           # Execute the update query
           cursor.execute(query, [name, code, price, id])
           connection.commit()
           print('Data Updated Successfully')

        except Exception as e:
            print('Something wrong, please check. Error:'+str(e))

        finally:
           # Close the connection
           connection.close()
