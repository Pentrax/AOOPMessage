from tests.test_base import BaseTestClass
import unittest


class LoginTestCase(BaseTestClass):

    def test_signup(self):
        res = self.client.get('/signup')

        print(f'\n\n RESPONSE {res}')
        self.assertEqual(200, res.status_code)

    def test_signup_post_user(self):
        res = self.client.post('/signup',
                               data={
                                     'email': 'test@user.com',
                                     'password': 'password'
                                     }
                               )
        self.assertEqual(200, res.status_code)


if __name__ == '__main__':
    unittest.main()
