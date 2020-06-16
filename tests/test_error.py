from tests.test_base import BaseTestClass
import unittest


class ErrorTestCase(BaseTestClass):

    def test_error(self):
        res = self.client.get('/path_not_existent')

        print(f'\n\n RESPONSE {res}')
        self.assertEqual(404, res.status_code)


if __name__ == '__main__':
    unittest.main()
