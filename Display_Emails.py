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
def Search():
	# make test list of email objects
	email = Email()
	email.sender = "Blue Duck" 
	email.subject = "I'm not chicken"
	email.body = " QUACK QUACK QUACK "
	email.date = "5/5/10"

	email2 = Email()
	email2.sender = "Red Duck" 
	email2.subject = "fart"
	email2.body = "lol"
	email2.date = "5/4/12"

	email3 = Email()
	email3.sender = "Green Duck" 
	email3.subject = "Yum"
	email3.body = "I want food"
	email3.date = "3/30/16"

	# stores emails from db into this Dictionary 
	Dictionary = {"Email_1": email, "Email_2": email2, "Email_3": email3}

	while (true):
		
		searchTerm = input("What would you like to search by?")

		if(searchTerm == "sender"):

		else if (searchTerm == "subject"):
		
		else if (searchTerm == "body"):
		
		else if (searchTerm == "date"):

		else:
			print("You fucked up")




	#print Dictionary["Email_1"].subject

	# pass them to search function in main


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
	#db = Get_Connection()
	#Prompt()
	Search()
	#Close_Connection(db)