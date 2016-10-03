#* PYTHON EMAIL PROJECT                 *#
#* Get_Emails.py                        *#
#* Fordham CSS September 25             *#
#* ------------------------------------ *#
#* Script to gather emails from server. *#

# IMPORTS
from Email_Object import Email # Email class to be used

import imaplib                 # Network Connection
import email                   # Email Parsing 
import getpass                 # Password Protection    
import re                      # Regular Expressions
import shelve                  # Databse Management

# PRE: Login Information from User
# POST: Connection to EMail Sever (connection)
# TODO: How to store user login?
# TODO: Make program more secure so Gmail stops seeing it as a threat. 
def Set_Connection():
    user = raw_input('Please enter your email address: ')
    password = getpass.getpass('Please enter your password: ')
    try:
        connection = imaplib.IMAP4_SSL('imap.gmail.com', 993)
        connection = imatlib.login(user, password)
        return connection

    # TODO: Better exception handling
    except Exception as e:
        print('Hit error')
        print e
    
# PRE: Database Exists
# POST: Database connection (db)
def DB_Connect():
    db = shelve.open('Emails.db')
    return db

# PRE: Connection with Server
# POST: List of Emails to Prioritize
def Get_Emails(conx):
    try:
        rsp, box = conx.select('INBOX', readonly=True)
        #TODO: change the search parameters to suite your own testing. 
        rsp, msg = conx.search(None, '(FROM "Nicholas DiBari" UNSEEN)')
        if(rsp == 'OK'):
            for ids in msg:
                rsp, msg_data = conx.fetch(ids, '(RFC822)')
                for rsp_part in msg_data:
                    if isinstance(rsp_part, tuple):
                        msg = email.message_from_string(rsp_part[1])
                        if(msg.is_multipart() == True):
                            print "Yes"
                        else:
                            print "Not"
    except Exception as e:    
        print('ERROR')
        print e
# PRE: List of Targeted Emails
# POST: Emails stored in Database 
def Store_Emails(Target_Emails):
    pass
    
# POST: Two list of Email objects
#       High_Priority contains emails from important sender and important emails
#       Low_Priority contains all other emails
def Set_Priority(EMAIL_LIST):
    pass
    
    # Loop through all emails
    for a in range(len(EMAIL_LIST)):
        pass
        # If the sender matches a sender in the user defined priority list
        # OR
        # If the sender address is from @fordham.edu
        # Then add to High_Priority
        
        # Else
        # Then add to Low_Priority

# PRE: One list of prioritized Emails to parse
# POST: One list of emails whose contents match common phrases for event sensitive emails
def Get_Targets(priority_list, Is_High_Priority):
    pass
    
# Main Driver
def Main(connection, db):
    Raw_Emails = Get_Emails(connection) # Look into returning a 3-tuple into an object. 


    pass

if __name__ == '__main__':
    connection = Set_Connection()
    db = DB_Connect()
    Main(connection, db)
