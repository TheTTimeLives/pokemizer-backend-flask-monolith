import unittest
import json
import pprint
from unittest import TestCase


# run with python -m unitttest file_name.py for just this file
# run with python -m unittest discover to discover all files prefixed with test and run them

whatever_data = [
    {
        'This' : 'That'
    },
    {
        'This' : 'That'
    },
    {
        'This' : 'That'
    }
]

# preface with test and it should run
class MyTest(TestCase):
    def test_some(self):
        # run some logic stuff
        self.assertEqual(len(whatever_data), 3)
