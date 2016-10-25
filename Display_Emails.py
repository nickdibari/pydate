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
	email = Email("Blue Duck", "5/5/10" , "I'm not chicken", " QUACK QUACK QUACK ", 235)
	email2 = Email("Red Duck", "5/4/12", "fart" , "lol yo" ,  2345) 
	email3 = Email("Green Duck", "3/30/16", "Yum" , "I want food" ,  3456)

	# stores emails from db into this Dictionary 
	Dictionary = {"Email_1": email, "Email_2": email2, "Email_3": email3}

	# Menu

	print ("What would you like to search for? Type the words in () ")
	print ("1. Search by sneder (sender)")
	print ("2. Search by subject (subject)")
	print ("3. Search for specfic word in body (body)")
	print ("4. Search by date (date)")

	while (True):
		searchTerm = raw_input("Please enter in term: ")
		print(searchTerm)   
		if searchTerm == "sender":
			senderTerm = raw_input("Please enter sender: ")
			for email in Dictionary.values():
				if email.sender == senderTerm:
					print (email)

		elif searchTerm == "subject":
			subjectTerm = raw_input("Please enter in subject: ")
			for email in Dictionary.values():
				if email.subject == subjectTerm:
					print (email)
		
		elif searchTerm == "body":
			bodyTerm = raw_input("Please enter in word in body of email you want to find: ")
			for email in Dictionary.values():
				if bodyTerm in email.body:
					print (email)
		
		
		elif searchTerm == "date":
			dateTerm = raw_input("Please enter date: ")
			for email in Dictionary.values():
				if email.date == dateTerm:
					print (email)

		else:
			print("You fucked up")

	#print Dictionary["Email_1"].subject

	# pass them to search function in main


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
	pass

# Main Prompt for User Interface
def Prompt(db):
	pass

if __name__ == '__main__':
	#db = Get_Connection()
	#Prompt()
	Search()
	#Close_Connection(db)
