from server import *

import requests,json
def test():
    # Set the API endpoint URL
        url = 'http://127.0.0.1:5000/get_riwayat_parkir'

        # Set the request headers
        headers = {"Content-Type": "image/jpeg"}
        
        response = requests.get(url)
        print(response.text)

if __name__ == '__main__':
    test()