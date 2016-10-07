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
def Get_Emails(RAW_EMAILS):
    pass

# PRE: List of Targeted Emails
# POST: Emails stored in Database 
def Store_Emails(Target_Emails):
    pass
    
# PRE: List of Email Objects
# POST: Two list of Email objects
#   High_Priority contains important emails
#   Low_Priority contains all other emails
#
# IMPORTANT: Must call function with assigning sequence set to 
# return value
# ex. High, Low = Set_Priority(EMAIL_LIST)
#
# TODO: More categories for adding emails to High_Priority
# TODO: Priority list of emails (Config file)
def Set_Priority(EMAIL_LIST):
    High_Priority = []
    Low_Priority = []
    keywords = ['Important', 'Urgent',  'Mandatory']

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
def Get_Targets(priority_list, Is_High_Priority):
    pass
    
# Main Driver
def Main():
    pass

if __name__ == '__main__':
    connection = Set_Connection()
    db = DB_Connect()
    Main()
