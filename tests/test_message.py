
from tests.test_base import BaseTestClass
import unittest


class SendMessageTestCase(BaseTestClass):



    def test_send_message_post_user(self):
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app.config['TESTING'] = True
        res = self.client.post('/send',
                               data={
                                    "title":"test tittle",
                                    "body":"test body message",
                                    "author_id":1,
                                    "to_id":2,
                                    "author_name":"user1@gmail.com",
                                    "to": "user2@gmail.com"
                                     }
                               )
        print(f'\n\n RESPONSE {res}')
        self.assertEqual(200, res.status_code)


if __name__ == '__main__':
    unittest.main()
