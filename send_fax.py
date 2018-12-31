import json
import os.path
import sys
from phaxio import PhaxioApi
from phaxio import SendFaxResponse


def send_fax(phone_number: str, filename: str) -> SendFaxResponse:

    api_key_dict = None

    if not os.path.exists("phaxio_key.json"):

        print("phaxio_key.json is not found!")
        exit(1)

    else:

        with open("phaxio_key.json", "r") as phaxio_key_obj:        
    
            api_key_dict = json.loads(phaxio_key_obj.read())
       
        phaxio = PhaxioApi(
            api_key_dict["api_key"], 
            api_key_dict["api_secret"]
        )

        return phaxio.Fax.send(
            to=phone_number, files=filename
        )


def main():

    if len(sys.argv) == 0 :

        print("python send_fax.py <PHONE NUMBER> <FILENAME>")
        exit(1)

    elif len(sys.argv) == 1:

        print("Either <PHONE NUMBER> or <FILENAME> is missing!")
        exit(1)
    
    elif len(sys.argv) > 2:

        print("Too many parameters!!!")
        exit(1)

    else:

        print(send_fax(sys.argv[0], sys.argv[1]))


