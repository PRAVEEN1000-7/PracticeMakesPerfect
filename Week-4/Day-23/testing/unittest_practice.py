import unittest
import string

def encrypt(message):
    ''' CaesarsCiphers algorithm for encypting message '''
    characters = string.ascii_letters + string.digits + string.punctuation + ' '
    encrypted_message = "".join([characters[characters.find(char)+1] for char in message])
    return encrypted_message

class TestEncryption(unittest.TestCase):
    
    def setUp(self):
        # setup message
        self.my_message = "Batman7!"
    
    def test_inputExists(self):
        # testing input existance
        self.assertIsNotNone(self.my_message)
    
    def test_inputType(self):
        # testing input type
        self.assertIsInstance(self.my_message, str)
        
    def test_functionReturns(self):
        # testing output existance
        self.assertIsNotNone(encrypt(self.my_message))
        
    def test_lenIO(self):
        # testing length of IO
        self.assertEqual(len(self.my_message),len(encrypt(self.my_message)))
        
    def test_differentIO(self):
        # testing Input and Output is not same
        self.assertNotIn(self.my_message, encrypt(self.my_message))
    
    def test_outputType(self):
        # testing output type
        self.assertIsInstance(encrypt(self.my_message), str)
    
if __name__ == "__main__":
    unittest.main()