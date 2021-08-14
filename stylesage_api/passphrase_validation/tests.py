from django.test import TestCase
from services import get_count_of_basic_valid_passphrases, get_count_of_valid_advanced_passphrases


class PassphraseValidatorTestCase(TestCase):
    def test_get_count_of_basic(self):
        passphrase_1 = '''
        aa bb cc dd
        aa bb cc dd aa
        aa bb cc dd aaa aa
        uu aa'''
        passphrase_2 = '''
        aa ff cc dd
        aa bb cc dd 
        aa bb cc dd aaa aa
        uu uu aa'''
        passphrase_3 = '''
        aa bb cc dd
        aa bb cc dd aa
        aa bb cc dd aaa aa
        uu uu aa'''

        self.assertEqual(get_count_of_basic_valid_passphrases(passphrase_1), 2)
        self.assertEqual(get_count_of_basic_valid_passphrases(passphrase_2), 2)
        self.assertEqual(get_count_of_basic_valid_passphrases(passphrase_3), 1)

    def test_get_count_advanced(self):
        passphrase_1 = '''
           abcde fghij
           abcde xyz ecdab
           '''
        passphrase_2 = '''
           a ab abc abd abf abj
           iiii oiii ooii oooi oooo
           cbc aaa bcc oiii
           '''
        passphrase_3 = '''
           oiii ioii iioi iiio
           aabb ccdd aaii
           aaii bbaa cc 
           '''
        self.assertEqual(get_count_of_valid_advanced_passphrases(passphrase_1), 1)
        self.assertEqual(get_count_of_valid_advanced_passphrases(passphrase_2), 2)
        self.assertEqual(get_count_of_valid_advanced_passphrases(passphrase_3), 2)




instance_basic_test = PassphraseValidatorTestCase()
print(instance_basic_test.test_get_count_of_basic())

instance_advanced_test = PassphraseValidatorTestCase()
print(instance_basic_test.test_get_count_advanced())
