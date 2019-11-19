#!/usr/bin/env python3
# coding: utf8

#
#   Modules imported
#
import urllib.request, json

#
#   Specific functions
#
def main(url, key):
    """
        Reads the content of a simple JSON object from HTTP
        @param {String} url: the URL to call
        @param {String} key: the key of the value to query
    """

    # Makes a request
    response = urllib.request.urlopen(url)

    # Gets the data
    data = response.read()

    # Reads it as a JSON object
    content = json.loads(data.decode("utf-8"))['value'][key]

    # Finally, prints it
    print(content)

#
#   Main
#
if __name__ == "__main__":

    # Configuration of the notifier
    config = {
        'url': 'http://api.icndb.com/jokes/random',
        'key': 'joke',
        'firstName': '',
        'lastName': ''
    }

    # If the keys firstName and lastName are not empty
    if config['firstName'] and config['lastName']:
        # The url is upgraded to retrieve a customized joke
        config['url'] = f'{config["url"]}?firstName={config["firstName"]}&lastName={config["lastName"]}'

    # Triggers the main() function
    main(config['url'], config['key'])
