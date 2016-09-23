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
# POST: Connection to EMail Sever
# TODO: How to create connection to server?
# TODO: How to store user login?
def Set_Connection():
    pass
    
# PRE: Connection with Server
# POST: List of Emails to Prioritize
def Get_Emails(RAW_EMAILS):
    pass

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
    Main()