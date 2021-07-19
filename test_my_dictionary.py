# The code to test
import unittest   # The test framework

class Test_my_dictionary(unittest.TestCase):
    def test_dictionary(self):
        self.assertEqual(word_check("help"), 1)

    def test_dictionary(self):
        self.assertEqual(word_check("paper"), None)

    def test_dictionary(self):
        self.assertEqual(word_check("abnormal"), 1)
    
    def test_dictionary(self):
        self.assertEqual(word_check("bottle"), None)

def word_check(check):
    my_dict = open("words.txt", "r")
    
    check = check.lower()
    contents = my_dict.read()
    contents=contents.split("\n")
    for line in contents:
        line = line.split(":")
       
        if check == line[0]:
            return 1

   
if __name__ == '__main__':
    unittest.main()
