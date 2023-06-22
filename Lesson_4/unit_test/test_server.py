
import os
import sys
import unittest

sys.path.append(os.path.join(os.getcwd(), '..'))

from common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR, MAX_CONNECTIONS
from server import process_client_message


class TestServer(unittest.TestCase):
    right_answer = {RESPONSE: 200}
    wrong_answer = {RESPONSE: 400, ERROR: 'Bad Request'}
    data = {
        ACTION: PRESENCE,
        TIME: 1,
        USER: {ACCOUNT_NAME: 'Aleks'}}

    def test_right_connection(self):
        self.assertEqual(process_client_message({ACTION: PRESENCE, TIME: 1, USER: {ACCOUNT_NAME: 'Guest'},
                                                 MAX_CONNECTIONS: 5}), self.right_answer)

    def test_no_action(self):
        test_data = {TIME: 1, USER: {ACCOUNT_NAME: 'Aleks'}}
        self.assertEqual(process_client_message(test_data), self.wrong_answer)

    def test_no_time(self):
        test_data = {ACTION: PRESENCE, USER: {ACCOUNT_NAME: 'Aleks'}}
        self.assertEqual(process_client_message(test_data), self.wrong_answer)

    def test_no_user(self):
        self.assertEqual(process_client_message({ACTION: PRESENCE, TIME: 1}), self.wrong_answer)

    def test_unknown_user(self):
        self.assertEqual(process_client_message({ACTION: PRESENCE, TIME: 1, USER: {ACCOUNT_NAME: 'NO_NAME'}}),
                         self.wrong_answer)


if __name__ == '__main__':
    unittest.main()