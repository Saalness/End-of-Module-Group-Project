"""Unit tests  cover the encryption/decryption, checking pickling format
"""
import unittest

from main import pickling_choice, encrypt_file, decrypt_file

class Testing(unittest.TestCase):

    def test_pickling(self):
       self.assertEqual(pickling_choice("xml", rxdic), output, "the output of the function should match the format chosen")

    def test_enc(self):
        self.assertEqual(encrypt_file("test.txt"), encrypted, "encryption was sucessful and file is secured")
        
    def test_dec(self):
        self.assertEqual(decrypt_file("text.txt", decrypted, "file was sucessfully decrypted"))

rxdic = {'Store Items': ['Fruits', 'Vegetables', 'Nuts'], 'Fruits': {'Mango': 6, 'Orange': 3, 'Apple': 50, 'Grapes': 15}, 'Vegetables': {
        'Sweet potatoes': 100, 'Spinach': 20, 'Carrot': 18}, 'Nuts': {'Almonds': 10, 'Cashews': 5, 'Walnuts': 150, 'Peanuts': 80}}

#not completed
output = ""
encrypted = ""
decrypted = ""