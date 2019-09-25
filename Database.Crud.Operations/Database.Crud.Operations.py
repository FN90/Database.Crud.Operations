import pyodbc
import db_connection as dbConn
from read import Read
from create import Create
from update import Update
from delete import Delete

def main():
    print('Available Options: C=Create, R=Read, U=Update, D=Delete ')
    choice = input('Choose your option = ')

    if choice == 'C':
        createObj=Create()
        createObj.create_data()
    elif choice == 'R':
        readObj =  Read()
        readObj.read_data()
    elif choice == 'U':
        updateObj = Update()
        updateObj.update_data()
    elif choice == 'D':
        deleteObj = Delete()
        deleteObj.delete_data()
    else:
        print('Wrong choice, You are going exist.')

# Call the main function
main()