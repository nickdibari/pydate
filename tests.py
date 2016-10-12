#* PYTHON EMAIL PROJECT                 *#
#* tests.py                        	*#
#* Fordham CSS September 25             *#
#* ------------------------------------ *#
#* Unit tests for PyDate program 	*#

from Email_Object import Email
from Get_Emails import Set_Priority

import unittest


# Unit Tests for Set_Priority function
class Test_Set_Priority(unittest.TestCase):
    # Test domain check
    def test_high_domain(self):
        email = Email()
        email.sender = 'test@fordham.edu'
        email.subject = 'Blah'
        EMAILS = [email]

        hi,lo = Set_Priority(EMAILS)

        self.assertEqual(len(hi),1)
        self.assertFalse(lo)

    # Test subject check
    def test_high_subject(self):
    	email = Email()
    	email.sender = 'test@test.com'
    	email.subject = 'Important'
    	EMAILS = [email]

    	hi,lo = Set_Priority(EMAILS)

    	self.assertEqual(len(hi),1)
    	self.assertFalse(lo)

    # Test default 
    def test_low_default(self):
    	email = Email()
    	email.sender = 'test@test.com'
    	email.subject = 'None'
    	EMAILS = [email]

    	hi,lo = Set_Priority(EMAILS)

    	self.assertEqual(len(lo),1)
    	self.assertFalse(hi)

    # Test Multiple cases
    def test_multi_cases(self):
    	email_sender = Email() #Important by sender
    	email_sender.sender = 'test@fordham.edu'
    	email_sender.subject = 'Blah'

    	email_subject = Email() #Important by subject
    	email_subject.sender = 'test@test.com'
    	email_subject.subject = 'Important'

    	email_lo = Email() #Not Important
    	email_lo.sender = 'test@test.com'
    	email_lo.subject = 'Blah'

    	EMAILS = [email_sender, email_subject, email_lo]

    	hi,lo = Set_Priority(EMAILS)

    	self.assertEqual(len(hi),2)
    	self.assertEqual(len(lo),1)

if __name__ == '__main__':
	unittest.main()

