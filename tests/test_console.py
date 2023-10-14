#!/usr/bin/python3
""" Test suite cases for console"""


import sys
import models
import unittest
from io import StringIO
from console import HBNBCommand
from unittest.mock import create_autospec


class test_console(unittest.TestCase):
    """ Test the console module"""

    def setUp(self):
        """set for """
        self.backup = sys.stdout
        self.capt_output = StringIO()
        self.stdout = self.capt_output