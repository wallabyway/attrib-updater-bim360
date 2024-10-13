import json
import requests
import os

# Set your environment variables for authentication
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

    # Querying model properties for the DWG file
    url = f"{APS_BASE_URL}/acc/v1/projects/{urn}/fields"
    headers = {
        'Authorization': f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    properties = response.json()

    # Example: Filter properties for a title block or other Revit category-related properties
    revit_properties = [prop for prop in properties['data'] if 'Revit' in prop['category']]

    return {
        'statusCode': 200,
        'body': json.dumps(revit_properties)
    }