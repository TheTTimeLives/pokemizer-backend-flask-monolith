from unittest import TestCase
import json
import pprint

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

class MyTest(TestCase):
    def some_test(self):
        # run some logic stuff
        self.assertEqual(len(whatever_data), 3)
