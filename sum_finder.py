import unittest

def find_low_sum_numbers(input):
    return (abs(input) * -1 -1, abs(input) * -1 - 2)

def find_low_sum_numbers_old(input):

    # input > 4
    if input > 4:
        return (1, 2)

    if input < 4 and input > 0:
        return (-1, -2)

    if input < 0:
        return (input - 1, input - 2)

class LowSumTests(unittest.TestCase):

    def test_5(self):
        input = 5
        result = find_low_sum_numbers(input)
        a = result[0]
        b = result[1]
        self.assertTrue((a + b) < input)

    def test_no_zeros(self):
        result = find_low_sum_numbers(10)
        self.assertFalse(result[0]==0 or result[1] == 0)

    def test_bigger_than_0_less_than_4(self):
        input = 3
        result = find_low_sum_numbers(input)
        a = result[0]
        b = result[1]
        self.assertTrue((a + b) < input)

    def test_negative_numbers(self):
        input = -1
        result = find_low_sum_numbers(input)
        a = result[0]
        b = result[1]
        self.assertTrue((a + b) < input)

def main():
    # Write a program to select two numbers
    # which sum is lower than a target number
    # If input is 4, answer could be 2 and 1.
    # If input is -2, answer could be -2, -1

    unittest.main()

main()

