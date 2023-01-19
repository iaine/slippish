import unittest
from slippish import Slippish

class TestSlippish (unittest.TestCase):

    def test_init_slippish(self):
        slip = Slippish()
        self.assertIsNotNone(slip.dll)

    def test_append(self):
        #Initialize the linked list with a new node
        slip = Slippish()
        slip.append(1)
        self.assertEqual(slip.dll.header, 1)

    def test_find(self):
        #Initialize the linked list with a new node
        slip = Slippish()
        slip.append(1)
        slip.append(2)
        find = slip.find(1)
        self.assertEqual(len(find), 1)
        self.assertEqual(find[0], 1)

    def test_empty_find(self):
        #Initialize the linked list with a new node
        slip = Slippish()
        slip.append(1)
        slip.append(2)
        find = slip.find(3)
        self.assertEqual(len(find), 0)

    def test_find_previous(self):
        #Initialize the linked list with a new node
        slip = Slippish()
        slip.append(1)
        slip.append(2)
        find = slip.find_previous(2)
        self.assertEqual(len(find), 1)
        self.assertEqual(find[0], 1) 

    def test_find_previous_value(self):
        #Initialize the linked list with a new node
        slip = Slippish()
        slip.append(1)
        slip.append(2)
        slip.append(10)
        find = slip.find_previous(2, relation="is", relation_value=10)
        self.assertEqual(len(find), 1)
        self.assertEqual(find[0], 1) 

    def test_send_osc_message (self):

        slip = Slippish()
        slip.send_osc("edge:261.25:0.5:0.25")

if __name__ == '__main__':
    unittest.main()