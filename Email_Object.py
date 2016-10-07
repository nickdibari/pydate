#!/usr/bin/python2.7       

#* EMAIL PROJECT PYTHON               *#
#* Email_Object.py                    *#
#* ---------------------------------- *#
#* Class Declaration for Email Object *#

class Email:
    def __init__(self):
        sender = " " # Sender of Email
        date = " " # Date Email was recieved
        subject = " " # Subject of Email
        body = " " # Body of email, should only be 250 characters

    def __str__(self):
    	return 'Sender: {0} \nSubject: {1} \nDate: {2} \nBody:\n{3}'\
    			.format(self.sender, self.subject, self.date, self.body)