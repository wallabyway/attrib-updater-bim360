# APS ACC DWG Properties to BIM360 Custom Attributes

This repository provides a Python Lambda function that retrieves properties ( Title Block Name, Description, etc) inside a DWG file, using Autodesk APS APIs, and then updates these as custom attributes in BIM360, using the BIM360 API's.

## Features

- **Retrieve DWG Properties**: Uses the Model Derivative API or Model Properties API to extract metadata (title block, description) from a DWG file.
- **Update BIM360 Custom Attributes**: Writes the retrieved key-value data to BIM360 using the BIM360 API.

### Setup (3 Steps)

1. Clone the repo:
   ```
   git clone github.com/wallabyway/attrib-updater-bim360
   ```

2. Install dependencies:
   ```
   pip install boto3 requests
   ```

3. Set environment variables (`CLIENT_ID`, `CLIENT_SECRET`) for Autodesk APS authentication.

### Lambda Function: Retrieve # Update DWG Properties

This Lambda function retrieves DWG metadata and writes it to BIM360 custom attributes.

```python
import json
import requests
import os

def get_access_token():
    # Obtain access token for APS API
    pass

def retrieve_dwg_properties(urn):
    # Retrieve title block and description using APS APIs
    # NOTE:
    # see fn_model_derivative_query.py to use the Model Derivative API
    # see fn_model_properties_query.py to use the Model Properties API
    pass

def update_bim360_attributes(project_id, folder_id, urn, kv_data, access_token):
    # Update BIM360 custom attributes
    # see fn_write_attributes.py for an example of how to do this
    pass

def lambda_handler(event, context):
    urn = event.get('urn')
    project_id = event.get('projectID')
    folder_id = event.get('folderID')
    access_token = get_access_token()
    
    # Retrieve DWG properties (title block, description)
    kv_data = retrieve_dwg_properties(urn)
    
    # Update BIM360 custom attributes
    update_bim360_attributes(project_id, folder_id, urn, kv_data, access_token)
    
    return {'statusCode': 200, 'body': json.dumps('Attributes updated successfully!')}
```