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
        connection.login(user, password)
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
# PRE: Connection with Server
# POST: List of Emails to Prioritize 
def Get_Emails(conx):
    Emails = []
    try:
        # TODO: Possibly extend to search other/all mailboxes.
        rsp, box = conx.select('INBOX', readonly=True)
        if(rsp == 'OK'): 
            rsp, msg = conx.search(None, '(UNSEEN)')           
            if(rsp == 'OK'):
                Msg_list = reversed(msg[0].split())
                for ids in Msg_list:
                    rsp, Msg_data = conx.fetch(ids, '(RFC822)')

                    if(rsp == 'OK'):
                        for rsp_part in Msg_data:
                            if isinstance(rsp_part, tuple):
                                msg = email.message_from_string(rsp_part[1]) 
                                tempEmail = Email()
                                tempEmail.subject = msg['subject']
                                tempEmail.sender = msg['from']
                                tempEmail.date = msg['date']
                                if(msg.is_multipart() == True):
                                    bodyText = msg.get_payload(0) 
                                    tempEmail.body = bodyText.get_payload(decode=True)
                                else:
                                    bodyText = msg.get_payload(decode=True)
                                    if type(bodyText) is str:
                                        tempEmail.body = bodyText
                                    else:
                                        # TODO: Further testing on single-part emails. 
                                        raise Exception('Single-part Payload not working')
                            
                                Emails.append(tempEmail)
                                if(len(Emails) == 100): 
                                    return Emails
    except Exception as e:    
        print('ERROR')                                                                      # TODO: Better exception handling.
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
def Main():
    pass

if __name__ == '__main__':
    connection = Set_Connection()
    db = DB_Connect()
    Main()
