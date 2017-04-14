import unittest
from ufrn.api import Ufrn


class TestUFRN(unittest.TestCase):

    def setUp(self):
        self.client_id = 'test'
        self.client_secret = 'test'
        self.grant_type = 'client_credentials'
        self.ufrn = Ufrn(self.client_id, self.client_secret)

    def test_ufrn_creation(self):
        self.assertTrue(isinstance(self.ufrn, Ufrn))

    def test_client_id(self):
        self.assertEqual(self.ufrn.client_id(), self.client_id)

    def test_client_secret(self):
        self.assertEqual(self.ufrn.client_secret(), self.client_secret)

    def test_grant_type(self):
        self.assertEqual(self.ufrn.grant_type(), self.grant_type)


if __name__ == '__main__':
    unittest.main()
