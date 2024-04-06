import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content  # Return the content as bytes-like object

    def load_json(self):
        response_body = self.get_response_body()
        response_body_str = response_body.decode('utf-8')  # Decode bytes to string
        return json.loads(response_body_str)  # Parse JSON string to Python dictionary
