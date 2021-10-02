import unittest
import USER_API

class TestYaApi(unittest.TestCase):

    def setUp(self):
        print('method setUp')

    def test_success_create_folder(self):
        self.assertEqual(USER_API.create_folder('test'), 201)

    def test_passed_create_folder(self):
        self.assertEqual(USER_API.create_folder('test_1'), 409)

    def tearDown(self):
        USER_API.delete_folder('test')
        print('method tearDown')

if __name__ == '__main__':
    unittest.main()