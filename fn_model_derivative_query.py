import json
import requests
import os

# Set your environment variables for authentication (or load from AWS Secrets Manager)
CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
APS_BASE_URL = 'https://developer.api.autodesk.com'

def get_access_token():
    url = f"{APS_BASE_URL}/authentication/v1/authenticate"
    payload = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'client_credentials',
        'scope': 'data:read'
    }
    response = requests.post(url, data=payload)
    response.raise_for_status()
    return response.json()['access_token']

def lambda_handler(event, context):
    # Extract URN from the input event
    urn = event.get('urn')
    if not urn:
        return {
            'statusCode': 400,
            'body': json.dumps('Missing URN')
        }
    
    access_token = get_access_token()

    # Querying the model for the Revit category properties
    url = f"{APS_BASE_URL}/modelderivative/v2/designdata/{urn}/metadata"
    headers = {
        'Authorization': f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    metadata = response.json()

    # Example: Filtering for title block
    revit_categories = [item for item in metadata['data']['metadata'] if 'Revit' in item['name']]

    return {
        'statusCode': 200,
        'body': json.dumps(revit_categories)
    }