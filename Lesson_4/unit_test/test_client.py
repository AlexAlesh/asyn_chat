
import os
import sys
import unittest

sys.path.append(os.path.join(os.getcwd(), '..'))

from common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR
from client import create_presence, process_ans


class TestClient(unittest.TestCase):

    def test_create_presence(self):
        test = create_presence()
        test[TIME] = 1
        self.assertEquals(test, {ACTION: PRESENCE, TIME: 1, USER: {ACCOUNT_NAME: 'Aleks'}})

    def test_process_ans_ok(self):
        self.assertEquals(process_ans({RESPONSE: 200}), '200 : OK')

    def test_process_ans_bad(self):
        self.assertEquals(process_ans({RESPONSE: 400, ERROR: 'Bad Request'}), '400 : Bad Request')

    def test_no_response(self):
        self.assertRaises(ValueError, process_ans, {ERROR: 'BAD REQUEST'})


