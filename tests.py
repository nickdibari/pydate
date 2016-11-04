#* PYTHON EMAIL PROJECT                 *#
#* tests.py                        	*#
#* Fordham CSS September 25             *#
#* ------------------------------------ *#
#* Unit tests for PyDate program 	*#

from Email_Object import Email
from Get_Emails import Set_Priority

import getpass
import unittest
import re

# Unit Tests for Set_Connection function
class Test_Set_Connection(unittest.TestCase):
    def setUp(self):
    self.user = raw_input('Please enter your email address: ')
    self.password = getpass.getpass('Please enter your password: ')

    def test_error_not_gmail(self):
        domain = re.search('@[\w.]+', self.user) 
        if domain.group[0] != '@gmail.com' or domain.group[0] != '@fordham':
            
'''
# Unit Tests for Set_Priority function
class Test_Set_Priority(unittest.TestCase):
    # Test domain check
    def test_high_domain(self):
        email = Email('test@fordham.edu', '', 'Blah', '', '')
        EMAILS = [email]

        hi,lo = Set_Priority(EMAILS)

        self.assertEqual(len(hi),1)
        self.assertFalse(lo)

    # Test subject check
    def test_high_subject(self):
    	email = Email('test@test.com', '', 'Important', '', '')
    	EMAILS = [email]

    	hi,lo = Set_Priority(EMAILS)

    	self.assertEqual(len(hi),1)
    	self.assertFalse(lo)

    # Test default 
    def test_low_default(self):
    	email = Email('test@test.com', '', 'None', '', '')
    	EMAILS = [email]

    	hi,lo = Set_Priority(EMAILS)

    	self.assertEqual(len(lo),1)
    	self.assertFalse(hi)

    # Test Multiple cases
    def test_multi_cases(self):
    	#Important by sender
        email_sender = Email('test@fordham.edu', '', 'Blah', '', '')

    	#Important by subject
        email_subject = Email('test@test.com', '', 'Important', '', '') 

    	#Not Important
        email_lo = Email('test@test.com', '', 'None', '', '') 
    	
    	EMAILS = [email_sender, email_subject, email_lo]

    	hi,lo = Set_Priority(EMAILS)

    	self.assertEqual(len(hi),2)
    	self.assertEqual(len(lo),1)
'''

if __name__ == '__main__':
	unittest.main()

