from test_base import BaseTestClass
import unittest


class IndexTestCase(BaseTestClass):

    def test_index(self):
        res = self.client.get('/')

        self.assertEqual(200, res.status_code)


if __name__ == '__main__':
    unittest.main()
