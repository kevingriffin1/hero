from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session
import requests

# Replace these values with your application's credentials
client_id = '139p54lm78j63ldjr2529ntpqn'
client_secret = 'gannob7l317n2cqmufa05q5rj0i0sev8kar3t5d2bvck723ivk8'
token_url = 'https://dev-nrel-research.auth.us-west-2.amazoncognito.com/oauth2/token'

# Prompt the user for their username and password
username = input('Enter your username: ')
password = input('Enter your password: ')

# Create an OAuth2 session
# oauth = OAuth2Session(client_id)
oauth = OAuth2Session(client=LegacyApplicationClient(client_id=client_id))

# Fetch the access token using Resource Owner Password Credentials Grant
try:
    token = oauth.fetch_token(
        token_url=token_url,
        username=username,
        password=password,
        client_id=client_id,
        client_secret=client_secret,
        verify=False,
        # grant_type='password'
    )
    print(f'Access Token: {token["access_token"]}')
except requests.exceptions.HTTPError as e:
    response_data = e.response.json()
    if 'mfa_required' in response_data:
        mfa_token = response_data['mfa_token']
        mfa_code = input('Enter the MFA code: ')

        # Resend the request with the MFA code
        mfa_data = {
            'grant_type': 'http://auth0.com/oauth/grant-type/mfa-otp',
            'client_id': client_id,
            'client_secret': client_secret,
            'mfa_token': mfa_token,
            'otp': mfa_code,
        }

        mfa_response = requests.post(token_url, data=mfa_data)
        mfa_response_data = mfa_response.json()

        if mfa_response.status_code == 200:
            print(f'Access Token: {mfa_response_data["access_token"]}')
        else:
            print(f'Failed to fetch token with MFA: {mfa_response_data}')
    else:
        print(f'Failed to fetch token: {response_data}')