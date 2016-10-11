#!/usr/bin/python2.7       

#* EMAIL PROJECT PYTHON               *#
#* Email_Object.py                    *#
#* ---------------------------------- *#
#* Class Declaration for Email Object *#

class Email:
    def __init__(self, sender, date, subject, body, id_code):
        self.sender = sender # Sender of Email
        self.date = date # Date Email was recieved
        self.subject = subject # Subject of Email
        self.body = body # Body of email
        self.id = id_code # Unique Email ID (use as key)

    def __str__(self):
    	return 'Sender: {0} \nSubject: {1} \nDate: {2} \nBody:\n{3}'\
    			.format(self.sender, self.subject, self.date, self.body)