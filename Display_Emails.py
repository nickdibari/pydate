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
	db = shelve.open('Emails.db')
	return db

# PRE: Databse connection
# POST: Emails displayed
def Print(db):
	pass

# PRE: Databse connection
# POST: Display Emails that fit criteria
def Search(db):
	matches = []
	flag = True

	# Menu
	print ("What would you like to search for? Type the words in () ")
	print ("--Search by sender (sender)")
	print ("--Search by subject (subject)")
	print ("--Search for specfic word in body (body)")
	print ("--Search by date (date)")

	# Get search term to search for and results
	while (flag):
		searchTerm = raw_input("Please enter in term: (Enter done to exit) ")
		
		if searchTerm == "sender":
			senderTerm = raw_input("Please enter sender: ")
			for email in db.values():
				if email.sender == senderTerm:
					matches.append(email)
				flag = False

		elif searchTerm == "subject":
			subjectTerm = raw_input("Please enter in subject: ")
			for email in db.values():
				if email.subject == subjectTerm:
					matches.append(email)
				flag = False
		
		elif searchTerm == "body":
			bodyTerm = raw_input("Please enter in word in body of email you want to find: ")
			for email in db.values():
				if bodyTerm in email.body:
					matches.append(email)
				flag = False
		
		elif searchTerm == "date":
			dateTerm = raw_input("Please enter date: ")
			for email in db.values():
				if email.date == dateTerm:
					matches.append(emails)
				flag = False
				
		elif searchTerm == "done":
			flag = False

		else:
			print("Invalid term, please try again")

	# Display matches
	if not matches:
		print('No matches')

	else:
		for match in matches:
			print match

# PRE: Database connection
# POST: Selected Emails deleted from Database
def Delete(db):
    #Print list of emails
    for key, value, in db.iteritems():
        print("Key term: " + key + "\nSender: " + value.sender + "\nSubject: " + value.subject)

    choice= raw_input("Please enter the key term of the email to delete: ")

    #Get email to delete
    email=db.get(choice)

    #Print quote to delete
    print("-----------------------------------------------")
    print('{0} :'.format(choice))
    print("Sender: " + db[choice].sender + "\nSubject: " + db[choice].subject)
    print("-----------------------------------------------")
    confirm = raw_input("Are you sure you want to do delete this email? (y/n): ")

    #Delete quote from dictionary
    if confirm == 'y' or confirm == 'Y':
        del db[choice]
        print("Deleted\n")

# PRE: Database connection
# POST: Database connection closed
def Close_Connection(db):
	db.close()

# Main Prompt for User Interface
def Prompt(db):
	pass

if __name__ == '__main__':
	db = Get_Connection()
	Prompt(db)
	Close_Connection(db)
