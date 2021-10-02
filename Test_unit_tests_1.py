import unittest
import mock
import builtins
from main import *

class Test_1(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    # ф-я проверки соответвия вывода владельца документа
    def test_get_doc_owner_name(self):
        with mock.patch.object(builtins, 'input', lambda _: 'p'):
            with mock.patch.object(builtins, 'input', lambda _: '11-2'):
                self.assertEqual(get_doc_owner_name(), 'Геннадий Покемонов')

    # ф-я добавления документа
    def test_add_new_doc(self):
        with mock.patch.object(builtins, 'input', lambda _: 'a'):
            with mock.patch.object(builtins, 'input', lambda _: '123'):
                with mock.patch.object(builtins, 'input', lambda _: 'pasport'):
                    with mock.patch.object(builtins, 'input', lambda _: 'stanislav'):
                        with mock.patch.object(builtins, 'input', lambda _: '4'):
                            self.assertEqual(add_new_doc(), '4')

if __name__ == '__main__':
    unittest.main()

