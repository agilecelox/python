import unittest

def reverse_string(input):

    if input == '':
        return input

    if input is None:
        raise ValueError('Invalid input: None')

    new_string = ''
    for i in range(len(input)):
        new_string += input[len(input) - i - 1]

    return new_string


class StringReverserTests(unittest.TestCase):

    def test_validate_string_reverse_happy_case(self):
        input = 'guillermo'
        output = 'omrelliug'
        result = reverse_string(input)
        self.assertEqual(output, result)

    def test_must_throw_on_none_input(self):
        with self.assertRaises(ValueError):
            reverse_string(None)

def main():
    unittest.main()

if __name__=='__main__':
    main()

