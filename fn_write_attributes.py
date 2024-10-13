import json
import requests
import os

# Set environment variables for authentication
CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
APS_BASE_URL = 'https://developer.api.autodesk.com'

def get_access_token():
    url = f"{APS_BASE_URL}/authentication/v1/authenticate"
    payload = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'client_credentials',
        'scope': 'data:write'
    }
    response = requests.post(url, data=payload)
    response.raise_for_status()
    return response.json()['access_token']

def lambda_handler(event, context):
    # Extract input data
    urn = event.get('urn')
    project_id = event.get('projectID')
    folder_id = event.get('folderID')
    kv_data = event.get('kv_data')
    access_token = event.get('access_token')

    if not urn or not project_id or not folder_id or not kv_data:
        return {
            'statusCode': 400,
            'body': json.dumps('Missing required input parameters')
        }

    # Write custom attributes to BIM360 API
    url = f"{APS_BASE_URL}/bim360/v1/projects/{project_id}/folders/{folder_id}/items/{urn}/attributes"
    headers = {
        'Authorization': f"Bearer {access_token}",
        'Content-Type': 'application/json'
    }

    payload = {
        'data': kv_data
    }

    response = requests.patch(url, headers=headers, json=payload)
    response.raise_for_status()

    return {
        'statusCode': 200,
        'body': json.dumps('Custom attributes updated successfully!')
    }