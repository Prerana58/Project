import json
import boto3
import base64
from io import BytesIO

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # Extract bucket name and file information from the event
    bucket_name = event.get('bucketName')
    file_name = event.get('fileName')
    file_content_base64 = event.get('fileContent')  # Base64 encoded content
    
    if not bucket_name or not file_name or not file_content_base64:
        return {
            'statusCode': 400,
            'body': json.dumps('Missing required parameters: bucketName, fileName, or fileContent')
        }
    
    # Decode the base64 file content
    file_content = base64.b64decode(file_content_base64)
    
    try:
        # Upload file to the specified S3 bucket
        s3_client.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=file_content,
            ContentType='application/pdf'  # Assuming the file is a PDF; adjust if necessary
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps('File uploaded successfully!')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error uploading file: {str(e)}')
        }
