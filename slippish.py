from doublelinkedlist import Node, DoublyLinkedList, DLLException
from yappyChuck import Client

class Slippish():

    def __init__(self):
        self.dll = DoublyLinkedList()

    def append (self, added):
        '''
            Add to a list
        '''
        self.dll.insert_at_end(added)

    def find (self, find_item):
        '''
            Find a value in the list. 
            Use it to get the list index for the value: useful for timings and repetition. 

            @param find_item
            @return list
        '''
        found = self.dll.search_list(find_item)

        return found

    def find_previous (self, find_item, relation="", relation_value=""):
        '''
            Find the related values for a value: useful for relationships

            @param find_item
            @return list
        '''
        found = self.dll.search_list_previous(find_item, relation="", relation_value="")

        return found

    def send_osc (self):
        '''
           Send an OSC message

           client.send("edge:261.25:0.5:3:0.25")
        '''
        client = Client()

        client.send("edge:261.25:0.5:3:0.25")