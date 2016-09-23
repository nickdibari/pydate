#! usr/bin/python2.7

#* PYTHON EMAIL PROJECT                 *#
#* Get_Emails.py                        *#
#* Ruhling, DiBari, Giroux             *#
#* ------------------------------------ *#
#* Script to gather emails from server. *#

# IMPORTS
from Email_Object import Email # Email class to be used
import imaplib                 # Network Connection
import email                   # Email Parsing 
import getpass                 # Password Protection    
import re                      # Regular Expression for Matching Targets

#* -----GIROUX SECTION----------------- *#
# PRE: Login Information from User
# POST: Connection to EMail Sever
def Set_Connection():
    print("In Set_Connection")
    
# PRE: Connection with Server
# POST: List of Emails to Prioritize
def Get_Emails(RAW_EMAILS):
    print("In Get_Emails")

#* -----RUHLING SECTION--------------- *#
# PRE: List of Targeted Emails
# POST: Emails stored in Database 
def Store_Emails(Target_Emails):
    print("In Store_Emails")
    
#* -----DIBARI SECTION----------------- *#
# Set_Priority
# PRE: One list of Email objects 
# POST: Two list of Email objects
#       High_Priority contains emails from important sender and important emails
#       Low_Priority contains all other emails
def Set_Priority(EMAIL_LIST):
    print("In Set_Priority")
    
    # Loop through all emails
    for a in range(len(EMAIL_LIST)):
        print("In For Loop of Set_Priority")
        # If the sender matches a sender in the user defined priority list
        # OR
        # If the sender address is from @fordham.edu
        # Then add to High_Priority
        
        # Else
        # Then add to Low_Priority

# Get_Targets
# PRE: One list of prioritized Emails to parse
# POST: One list of emails whose contents match common phrases for event sensitive emails
def Get_Targets(priority_list, Is_High_Priority):
    print("In Get_Targets")
    
