# a simple program to demonstrate how to make a connection to a server and get a response
# using json responses from a server and then parsing the response to get the data we need
from urllib.request import urlopen
import json


def main():
    url = "your url here"
    
    # make a connection to the server and get response
    with urlopen(url) as response:
        # parse the response and convert it to a list of dictionaries
        data = json.loads(''.join([line.decode() for line in response.readlines()]))

    print(data)


if __name__ == "__main__":
    main()