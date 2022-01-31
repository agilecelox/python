import unittest


def is_palindrome(input):
    '''
    Given an integer, determine if it is a palindrome
    :param input: input integer
    :return: True is it is a palindrome, False if not
    '''

    if input < 10:
        return True

    str_rep = str(input)
    length = int(len(str_rep))
    for index in range(int(length / 2)):
        if str_rep[index] != str_rep[length - index - 1]:
            return False

    return True

class PalindromeTests(unittest.TestCase):

    def test_101_must_pass(self):
        input = 101
        result = is_palindrome(input)
        self.assertTrue(result)

    def test_102_must_fail(self):
        input = 102
        result = is_palindrome(input)
        self.assertFalse(result)

    def test_9_must_pass(self):
        input = 9
        result = is_palindrome(input)
        self.assertTrue(result)

unittest.main()