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
# PRE: Connection with Server
# POST: List of Emails to Prioritize 
def Get_Emails(conx):
    Emails = []
    try:
        rsp, box = conx.select('INBOX', readonly=True)                                  # <--- TODO: Possibly extend to search other/all mailboxes.
        if(rsp == 'OK'): 
            rsp, msg = conx.search(None, '(UNSEEN)')                                    # msg[0] is a string of the message IDs found in the search
            
            if(rsp == 'OK'):
                Msg_list = reversed(msg[0].split())                                     # The string is split and reversed so Msg_list contains a set 
                                                                                        # starting with the newest email.

                for ids in Msg_list:
                    rsp, Msg_data = conx.fetch(ids, '(RFC822)')                         # Returns a response code and a set of the emails 
                                                                                        # of the provided IDs in RFC2822 format.

                    if(rsp == 'OK'):
                        for rsp_part in Msg_data:
                            if isinstance(rsp_part, tuple):
                                msg = email.message_from_string(rsp_part[1])            #Create a email.message object from a string. 
                                tempEmail = Email()



                                tempEmail.subject = msg['subject']                      # **********************************************************
                                tempEmail.sender = msg['from']                          # ** Populate the variables of the temporary Email object ** 
                                tempEmail.date = msg['date']                            # **********************************************************


                                if(msg.is_multipart() == True):                         # If the email message is a multi-part email you must get the 
                                    bodyText = msg.get_payload(0)                       # get the payload as a string so it can be decoded. 
                                    tempEmail.body = bodyText.get_payload(decode=True)
                                else:
                                    bodyText = msg.get_payload(decode=True)
                                    if type(bodyText) is str:
                                        tempEmail.body = bodyText
                                    else:
                                        raise Exception('Single-part Payload not working')  # TODO: Further testing on single-part emails. 
                                

                                Emails.append(tempEmail)
                                if(len(Emails) == 100):                                     # The set of Email objects is set to return at 100 because 
                                    return Emails                                           # of an issue with timing out. 


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
def Main(connection, db):
    Raw_Emails = Get_Emails(connection) # Look into returning a 3-tuple into an object. 


    pass

if __name__ == '__main__':
    connection = Set_Connection()
    db = DB_Connect()
    Main(connection, db)
