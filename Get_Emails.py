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
from datetime import datetime  # Datetime Information

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
    db = shelve.open('Emails.db', writeback=True)
    return db

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
                                msgid = msg['message-id']
                                subject = msg['subject']
                                sender = msg['from']
                                date = msg['date']
                                if(msg.is_multipart() == True):
                                    bodyText = msg.get_payload(0) 
                                    body = bodyText.get_payload(decode=True)
                                else:
                                    bodyText = msg.get_payload(decode=True)
                                    if type(bodyText) is str:
                                        body = bodyText
                                    else:
                                        # TODO: Further testing on single-part emails. 
                                        raise Exception('Single-part Payload not working')
                                tempEmail = Email(sender, date, subject, body, msgid)
                                Emails.append(tempEmail)
                                if(len(Emails) == 100): 
                                    return Emails
                return Emails
    # TODO: Better exception handling.
    except Exception as e:    
        print('ERROR')
        print e
        
# PRE: List of Targeted Emails
# POST: Emails stored in Database 
def Store_Emails(Target_Emails, db):
    #Save contents of list to shelve db
    for i in range(len(Target_Emails)):
        db[str(datetime.now())] = Target_Emails[i] # TODO: Consider different key. Maybe include info on sender?        
    
# PRE: List of Email Objects
# POST: Two list of Email objects
#   High_Priority contains important emails
#   Low_Priority contains all other emails
#
# IMPORTANT: Must call function with assigning sequence set to 
# return value
# ex. High, Low = Set_Priority(EMAIL_LIST)
#
# TODO: More categories for prioritizing emails
# TODO: Priority list of emails (Config file)
def Set_Priority(EMAIL_LIST):
    High_Priority = []
    Low_Priority = []
    keywords = ['Important', 'Urgent', 'Mandatory', 'Notice', 'Alert']

    for email in EMAIL_LIST:
        # Sender from '@fordham.edu'
        domain = re.search('@[\w.]+', email.sender)
        if domain.group(0) == '@fordham.edu':
            High_Priority.append(email)
        
        # Keywords in Subject
        elif any(keyword in email.subject for keyword in keywords):
            High_Priority.append(email)
        
        else:
            Low_Priority.append(email)

    return High_Priority, Low_Priority

# PRE: One list of prioritized Emails to parse
# POST: One list of emails whose contents match common phrases for event sensitive emails
def Get_Targets(EMAIL_LIST, Is_High_Priority):
    priority_emails = []
    cancel_keywords = ['class cancelled', 'class canceled']
    due_keywords = ['due', 'assignment', 'homework']
    
    # High Priority Checks
    if Is_High_Priority:
        for email in EMAIL_LIST:
            # Check subject for class cancellation
            if any(keyword in email.subject.lower() for keyword in cancel_keywords):
                priority_emails.append(email)

            # Check subject for assignment info
            elif any(keyword in email.subject.lower() for keyword in due_keywords):
                priority_emails.append(email)

    # All other checks
    for email in EMAIL_LIST:
        if email.body:
            # Check for date
            match = re.search(r'(([A-Z][a-z]*)\s([0-9].),\s([0-9]{2,4}))', email.body, flags=0)
            if match:
                priority_emails.append(email)
            else:
                # Check for time
                match = re.search(r'(([0-9].):([0-9].))', email.body, flags=0)
                if match:
                    priority_emails.append(email)

    return priority_emails
    
# Main Driver
def Main():
    connection = Set_Connection()
    db = DB_Connect()

    RAW_EMAILS = Get_Emails(connection)
    Hi, Lo = Set_Priority(RAW_EMAILS)

    if Hi:
        targets = Get_Targets(Hi, True)
        targets.extend(Get_Targets(Lo[:100], False))

    else:
        targets = Get_Targets(Lo, False)

    Store_Emails(targets, db)
    db.sync()

    connection.close()
    connection.logout()
    db.close()

if __name__ == '__main__':
    Main()
