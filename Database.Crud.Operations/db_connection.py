import pyodbc

# create database connection
def getConnection():
    connection = pyodbc.connect('Driver={SQL Server};'
                      'Server=YOUR_SERVER_NAME;'
                      'Database=Python.Crud.Operations;'
                      'Trusted_Connection=yes;')
    return connection 