#* PYTHON EMAIL PROJECT                 *#
#* Get_Emails.py                        *#
#* Fordham CSS September 25             *#
#* ------------------------------------ *#
#* Script to print Emails from Database *#

#IMPORTS
from Email_Object import Email # Email class to be used

import shelve				   # Database Management

# PRE: Databse exists
# POST: Database connection (db)
# TODO: Clean up database here?
#		-> Remove events that have already passed
def Get_Connection():
	pass

# PRE: Databse connection
# POST: Emails displayed
def Print(db):
	pass

# PRE: Databse connection
# POST: Display Emails that fit criteria
def Search(db):
	pass
	print "Hello"
	print "Hey"

# PRE: Database connection
# POST: Selected Emails deleted from Database
def Delete(db):
	pass

# PRE: Database connection
# POST: Database connection closed
def Close_Connection(db):
	pass

# Main Prompt for User Interface
def Prompt(db):
	pass

if __name__ == '__main__':
	db = Get_Connection()
	Prompt(db)
	Close_Connection(db)