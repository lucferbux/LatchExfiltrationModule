from exfiltration_reader import LatchExfiltrationReader
from exfiltration_writer import LatchExfiltrationWriter
from latch_interface import LatchInterface
import os
import argparse

def main():
    args = create_arguments()
    if args.account_id:
        latch = LatchInterface()
        account_id = latch.pair_latch(args.account_id)
        if account_id:
            print('''This is the account_id for your latch application, it will be used in this session, pleas add it  as an enviroment variable called 'LATCH_ACCOUNT_ID' ---> ''' + account_id)
            print('--------------------------')
            print('')
        else:
            print('Error pairing account_id, try again')
            return
    try:
        account_id = os.environ['LATCH_ACCOUNT_ID']
    except:
        print('Error, no account id provided, please add it as an enviroment variable or paira new account with flag -a')
        return

    if args.writer:
        message = args.writer if args.writer else ""
        latch_writer = LatchExfiltrationWriter()
        latch_writer.exfiltrate_message(message)
    elif args.reader:
        latch_reader = LatchExfiltrationReader()
        latch_reader.read_exfiltrated_message()


def create_arguments():
    parser = argparse.ArgumentParser(description="This script exfiltrates a message throughout the Latch Platform")
    parser.add_argument('-a', '--account_id', help='Flag to pair latch to account_id with pairing key (needed app_id and app_secret in enviromental variables')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-w', '--writer', help='Writes a message to sent to a reader node')
    group.add_argument('-r', '--reader', action='store_true', help='Read the message the writer module is sending')
    return parser.parse_args()  

if __name__ == "__main__":
    main()

