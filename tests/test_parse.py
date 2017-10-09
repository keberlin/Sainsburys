import unittest

from parse import *

class TestCases(unittest.TestCase):

  def test_find_day(self):
    header = ['mon','tue','wed-fri','description']
    answer = find_day('mon', header)
    self.assertEqual(answer, 0)
    answer = find_day('tue', header)
    self.assertEqual(answer, 1)
    answer = find_day('wed', header)
    self.assertEqual(answer, 2)
    answer = find_day('thu', header)
    self.assertEqual(answer, 2)
    answer = find_day('fri', header)
    self.assertEqual(answer, 2)

    header = ['description','mon-wed','thu','fri']
    answer = find_day('mon', header)
    self.assertEqual(answer, 1)
    answer = find_day('tue', header)
    self.assertEqual(answer, 1)
    answer = find_day('wed', header)
    self.assertEqual(answer, 1)
    answer = find_day('thu', header)
    self.assertEqual(answer, 2)
    answer = find_day('fri', header)
    self.assertEqual(answer, 3)

  def test_process_file(self):
    filename = '1.csv'
    results = process_file(filename)
    expected = [{'day': 'mon', 'description': 'first_desc 1', 'square': 1, 'value': 1},  {'day': 'tue', 'description': 'first_desc 25', 'square': 25, 'value': 5},  {'day': 'wed', 'description': 'first_desc 4', 'square': 4, 'value': 2},  {'day': 'thu', 'description': 'first_desc 6', 'double': 6, 'value': 3},  {'day': 'fri', 'description': 'first_desc 6', 'double': 6, 'value': 3}]
    self.assertEqual(results,expected)
    filename = '2.csv'
    results = process_file(filename)
    expected = [{'day': 'mon', 'description': 'second_desc 4', 'square': 4, 'value': 2},  {'day': 'tue', 'description': 'second_desc 4', 'square': 4, 'value': 2},  {'day': 'wed', 'description': 'second_desc 4', 'square': 4, 'value': 2},  {'day': 'thu', 'description': 'second_desc 4', 'double': 4, 'value': 2},  {'day': 'fri', 'description': 'second_desc 6', 'double': 6, 'value': 3}]
    self.assertEqual(results,expected)
    filename = '3.csv'
    results = process_file(filename)
    expected = [{'day': 'mon', 'description': 'third_desc 9', 'square': 9, 'value': 3},  {'day': 'tue', 'description': 'third_desc 9', 'square': 9, 'value': 3},  {'day': 'wed', 'description': 'third_desc 4', 'square': 4, 'value': 2},  {'day': 'thu', 'description': 'third_desc 4', 'double': 4, 'value': 2},  {'day': 'fri', 'description': 'third_desc 2', 'double': 2, 'value': 1}]
    self.assertEqual(results,expected)
