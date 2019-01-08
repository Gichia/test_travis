'''A class to represent the user model'''
import unittest
import travis


class TestPassword(unittest.TestCase):
    '''A class to represent the user model'''

    def test_length(self):
        '''A class to represent the user model'''
        self.assertEqual(travis.validate('eyThere123$'), True)

    def test_has_lowercase(self):
        '''A class to represent the user model'''
        self.assertEqual(travis.validate('Hthere#123ey'), True)

    def test_has_uppercase(self):
        '''A class to represent the user model'''
        self.assertEqual(travis.validate('@heyh1tyH'), True)

    def test_special_charcters(self):
        '''A class to represent the user model'''
        self.assertEqual(travis.validate('thj567$KL@'), True)
    
    def test_has_numerics(self):
        '''A class to represent the user model'''
        self.assertEqual(travis.validate('PeTer1##'), True)


if __name__ == '__main__':
    unittest.main()
    