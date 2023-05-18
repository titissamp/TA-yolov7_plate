from server import *
import time

import requests,json
def test():
    # Set the API endpoint URL
    
        start_time = time.time()
        url = 'http://127.0.0.1:5000/upload'

        # Set the request headers
        headers = {"Content-Type": "image/jpeg"}
        
        response = requests.post(url)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(response.text)    
        print(f"Elapsed time: {elapsed_time} seconds")

if __name__ == '__main__':
    test()