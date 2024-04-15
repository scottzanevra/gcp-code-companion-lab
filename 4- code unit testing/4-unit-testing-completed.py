
# function that extracts and email address using regex from a string

def extract_email(string):
    pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
    return  pattern

import unittest
import re

class TestExtractEmail(unittest.TestCase):

    def test_valid_email(self):
        string = "This is a test email: example@example.com"
        pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
        result = pattern.findall(string)
        self.assertEqual(result, ['example@example.com'])

    def test_invalid_email(self):
        string = "This is a test email: example"
        pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
        result = pattern.findall(string)
        self.assertEqual(result, [])

    def test_multiple_emails(self):
        string = "This is a test email: example@example.com, example2@example.com"
        pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
        result = pattern.findall(string)
        self.assertEqual(result, ['example@example.com', 'example2@example.com'])

    def test_empty_string(self):
        string = ""
        pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
        result = pattern.findall(string)
        self.assertEqual(result, [])



# function that does a inner join between two lists

def inner_join(list1, list2):
    result = []
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                result.append(item1)
    return result


import unittest

class TestInnerJoin(unittest.TestCase):

    def test_empty_lists(self):
        list1 = []
        list2 = []
        result = inner_join(list1, list2)
        self.assertEqual(result, [])

    def test_single_element_lists(self):
        list1 = [1]
        list2 = [2]
        result = inner_join(list1, list2)
        self.assertEqual(result, [])

        list1 = [1]
        list2 = [1]
        result = inner_join(list1, list2)
        self.assertEqual(result, [1])

    def test_multiple_element_lists(self):
        list1 = [1, 2, 3]
        list2 = [2, 3, 4]
        result = inner_join(list1, list2)
        self.assertEqual(result, [2, 3])

    def test_duplicate_elements(self):
        list1 = [1, 2, 2, 3]
        list2 = [2, 3, 3, 4]
        result = inner_join(list1, list2)
        self.assertEqual(result, [2, 3])
