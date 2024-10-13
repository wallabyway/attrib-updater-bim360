import json
import boto3
import requests
import os

def lambda_handler(event, context):
    # Parse the webhook payload
    if 'body' in event:
        webhook_data = json.loads(event['body'])
        print("Webhook Data: ", webhook_data)
    
        # Extract relevant information
        if 'data' in webhook_data:
            file_name = webhook_data['data'].get('fileName', 'Unknown')
            project_id = webhook_data['data'].get('projectId', '')
            file_id = webhook_data['data'].get('fileId', '')
            folder_id = webhook_data['data'].get('folderId', '')
            
            print(f"New DWG File Uploaded: {file_name}, Project: {project_id}")
            
            # Call another function or processing logic here
            # Example: You can trigger the next Lambda or process this data further
            # process_dwg_file(file_name, project_id, file_id, folder_id)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Webhook received successfully!')
    }