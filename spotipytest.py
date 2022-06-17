#https://www.youtube.com/watch?v=xdq6Gz33khQ


import requests
import base64
import datetime

client_id = 'e52866d90e6f4ad1a4f9a01d7cc29adc'
client_secret = 'cbe0798595c844fb8a75c591051d0fc8'

token_url = 'https://accounts.spotify.com/api/token'
METHOD = 'POST'

client_creds = f"{client_id}:{client_secret}"
client_creds_b64 = base64.b64encode(client_creds.encode())

token_data = {
    "grant_type":"client_credentials"
    }
token_header = {
    "Authorization": f"Basic {client_creds_b64.decode()}" #<base64 encoded client_id:client_secret>
    }




class SpotifyAPI(object):
    access_token = None
    access_token_expires = datetime.datetime.now()
    access_token_did_expire = True
    client_id =  None
    client_secret = None
    token_url = 'https://accounts.spotify.com/api/token'

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def get_client_credentials(self):
        """
        Returns base64 encoded string
        """
        client_id = self.client_id
        client_secret = self.client_secret
        client_creds = f"{client_id}:{client_secret}"
        client_creds_b64 = base64.b64encode(client_creds.encode())
        return client_creds_b64.decode()

    def get_token_header(self):
        client_creds_b64 = self.get_client_credentials()
        return {
            "Authorization": f"Basic {client_creds_b64.decode()}" #<base64 encoded client_id:client_secret>
            }

    def get_token_data(self):
        return {
            "grant_type":"client_credentials"
            }

    def perform_auth(self):
        token_url = self.token_url
        token_data = self.get_token_data()
        token_header = self.get_token_header()

        r = requests.post(token_url, data = token_data, headers = token_header)
        print(r.json())
        valid_request = r.status_code in range(200, 299)
        if not valid_request:
            return False
        data = r.json()
        access_token = data['access_token']
        self.access_token = access_token
        expires_in = data['expires_in']

        now = datetime.datetime.now()
        expires = now + datetime.timedelta(seconds = expires_in)
        self.access_token_expires = expires
        self.access_token_did_expire = expires < now
        return True


def main():
    client = SpotifyAPI(client_id, client_secret)
    client.perform_auth()
    print(client.access_token())
