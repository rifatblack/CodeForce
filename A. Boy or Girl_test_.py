import unittest

class TestStringMethods(unittest.TestCase):

    def test1(self):
        def main():
            s1 = input()  # String.
            s1 = dict.fromkeys(s1)  # Convert it to dictionary to remove duplicates.

            if len(s1) % 2 == 0:
                print("CHAT WITH HER!")
            else:
                print("IGNORE HIM!")

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()