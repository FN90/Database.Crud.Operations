import pyodbc

# create database connection
def getConnection():
    connection = pyodbc.connect('Driver={SQL Server};'
                      'Server=HS052-w2k12;'
                      'Database=SupportEmailExplorer;'
                      'Trusted_Connection=yes;')
    return connection 