import unittest
import mock
import builtins
from unittest.mock import patch
from main import *

class Test_1(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # ф-я проверки соответвия вывода владельца документа
    @patch('builtins.input', side_effect=['11-2', 'Геннадий Покемонов'])
    def test_get_doc_owner_name(self,mock_input):
        self.assertEqual(get_doc_owner_name(), 'Геннадий Покемонов')

    # ф-я добавления документа
    @patch('builtins.input', side_effect=['123', 'passport', 'stanislav', '4'])
    def test_add_new_doc(self,mock_input):
        self.assertEqual(add_new_doc(), '4')

    # ф-я проверки вывода №  полки
    @patch('builtins.input', side_effect=['11-2'])
    def test_get_doc_shelf(self, mock_input):
        self.assertEqual(get_doc_shelf(), '1')

    # ф-я проверки вывода cписка владельцев документов
    def test_get_all_doc_owners_names(self):
        self.assertEqual(get_all_doc_owners_names(),{'Василий Гупкин', 'Геннадий Покемонов', 'Аристарх Павлов','stanislav'})

    # ф-я проверки удаления № документа
    @patch('builtins.input', side_effect=['11-2'])
    def test_delete_doc(self,mock_input):
        self.assertEqual(delete_doc(),'11-2')

if __name__ == '__main__':
    unittest.main()