import unittest
from doublelinkedlist import Node, DoublyLinkedList, DLLException

class TestDLLTests (unittest.TestCase):

    def test_create(self):
        #Initialize the linked list with a new node
        doublyLL = DoublyLinkedList()
        self.assertEqual(doublyLL.header, 0)

    def test_insert_one_element(self):
        doublyLL = DoublyLinkedList()
        doublyLL.insert_in_emptylist(50)
        self.assertEqual(doublyLL.header, 1)

    def test_raise_error_insert_one_element_into_non_empty(self):
        doublyLL = DoublyLinkedList()
        doublyLL.insert_in_emptylist(50)
        self.assertRaises(DLLException, doublyLL.insert_in_emptylist, 51)

    def test_insert_at_start_empty_list(self):
        doublyLL = DoublyLinkedList()
        doublyLL.insert_at_start(4)
        self.assertEqual(doublyLL.header, 1)
        items = [node.item for node in doublyLL]
        self.assertEqual(items[0], 4)

    def test_insert_at_start_empty(self):
        doublyLL = DoublyLinkedList()
        doublyLL.insert_in_emptylist(50)
        doublyLL.insert_at_start(4)
        self.assertEqual(doublyLL.header, 2)
        items = [node.item for node in doublyLL]
        self.assertEqual(items[0], 4)

    def test_insert_at_start_(self):
        doublyLL = DoublyLinkedList()
        doublyLL.insert_at_start(50)
        doublyLL.insert_at_start(4)
        self.assertEqual(doublyLL.header, 2)
        items = [node.item for node in doublyLL]
        self.assertEqual(items[0], 4)

    def test_insert_at_end_empty(self):
        doublyLL = DoublyLinkedList()
        doublyLL.insert_at_end(4)
        self.assertEqual(doublyLL.header, 1)
        items = [node.item for node in doublyLL]
        self.assertEqual(items[0], 4)

    def test_insert_at_end_with_list_one_item(self):
        doublyLL = DoublyLinkedList()
        doublyLL.insert_at_end(4)
        self.assertEqual(doublyLL.header, 1)
        items = [node.item for node in doublyLL]
        self.assertEqual(items[len(items)-1], 4)

    def test_insert_at_end_with_more_than_one(self):
        doublyLL = DoublyLinkedList()
        doublyLL.insert_at_end(10)
        self.assertEqual(doublyLL.header, 1)
        doublyLL.insert_at_end(4)
        self.assertEqual(doublyLL.header, 2)
        items = [node.item for node in doublyLL]
        self.assertEqual(items[len(items)-1], 4)

    def test_search_list_one_entry(self):
        doublyLL = DoublyLinkedList()
        doublyLL.insert_at_start(7)
        search = doublyLL.search_list(7)
        self.assertEqual(len(search), 1)
        self.assertEqual(search[0], 1)

    def test_search_list_multiple_entries(self):
        doublyLL = DoublyLinkedList()
        doublyLL.insert_at_start(9)
        doublyLL.insert_at_end(9)
        search = doublyLL.search_list(9)
        self.assertEqual(len(search), 2)
        self.assertEqual(search[len(search)-1], 2)

    def test_search_previous(self):
        doublyLL = DoublyLinkedList()
        doublyLL.insert_at_start(9)
        doublyLL.insert_at_end(10)
        search = doublyLL.search_list_previous(10)
        self.assertEqual(search[0], 9)  

if __name__ == '__main__':
    unittest.main()