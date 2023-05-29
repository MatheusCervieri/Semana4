from io import BytesIO
import json
import base64
import boto3
import uuid

def post_handler(event, context):
    # get the base64-encoded body
    base64_image = event.get('body', '')

    # decode the image
    image_data = base64.b64decode(base64_image)
    file_name = f'{uuid.uuid4()}.jpg'   

    
    # create a boto3 client
    #s3_connection = boto3.client('s3', endpoint_url='http://localhost:4510')

    # specify your bucket name and generate a unique file name
     # creates a unique name

    # upload the image to S3
    #s3_connection.create_bucket(Bucket='mybucket')
    #s3_connection.upload_fileobj(BytesIO(image_data), 'mybucket', file_name)

    response = {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*', 
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,PUT,DELETE'
        },
        'body': f'Image {file_name} uploaded to S3 successfully'
    }
    return response

# Listar arquivos do bucket
# awslocal s3 ls s3://mybucket

# awslocal s3 rm s3://mybucket/his.flac

# limpar o bucket
# awslocal s3 rm s3://mybucket --recursive

def create_bucket_if_not_exists(bucket_name):
    s3_client = boto3.client('s3')
    try:
        s3_client.head_bucket(Bucket=bucket_name)
    except s3_client.exceptions.NoSuchBucket:
        s3_client.create_bucket(Bucket=bucket_name)