import unittest
from ptpbot import PTPBot


class TestPTPBot(unittest.TestCase):

    def setUp(self):
        self.ptpbot = PTPBot('Testing the PTPBot')

    def test_get_comments_from_winning_submission(self):
        pass
