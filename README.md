### LATCH EXFILTRATION MODULE  ###


#### PREREQUISITES LATCH ####

* Python.

* Read API documentation (https://latch.elevenpaths.com/www/developers/doc_api).

* To get the "Application ID" and "Secret", (fundamental values for integrating Latch in any application), it’s necessary to register a developer account in Latch's website: https://latch.elevenpaths.com. On the upper right side, click on "Developer area".

* Add the "Application ID" ['LATCH_APP'] and "Secret" ['LATCH_SECRET'] to your enviroment variables, if you have and "Account ID" ['LATCH_ACCOUNT_ID'], add it too, if not, pair with the script



#### USING THE SCRIPT ####

* In the Exfiltration module, write in your terminal:
```
	python latch_exfiltration_script.py -h
```

* This will expand the help menu:
```
	usage: latch_exfiltration_script.py [-h] [-a ACCOUNT_ID] (-w WRITER | -r)

    This script exfiltrates a message throughout the Latch Platform

    optional arguments:
    -h, --help            show this help message and exit
    -a ACCOUNT_ID, --account_id ACCOUNT_ID
                            Flag to pair latch to account_id with pairing key
                            (needed app_id and app_secret in enviromental
                            variables
    -w WRITER, --writer WRITER
                            Writes a message to sent to a reader node
    -r, --reader          Read the message the writer module is sending
```

* To add an account id, write in the terminal:
```
	python latch_exfiltration_script.py -a [pairing key] -r/-w
```

* This will add the enviroment variable throught the execution of the script, add it later to your enviroment variables with the key ['LATCH_ACCOUNT_ID']


