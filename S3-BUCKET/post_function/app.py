from io import BytesIO
import json
import base64
import boto3
import uuid

# Criar um portal estático no S3 que receba um arquivo e armazene-o
# fazer usando lambda -
# fazer usando API Gateway

# This is your AWS Lambda function handler.
# AWS Lambda calls this function with two arguments: event and context.
def post_handler(event, context):

    # Print out a message indicating that the function is running.
    print("Olá, nos estamos usando o S3 dentro do localstack, por isso, você precisa criar um bucket no seu localstack com o nome bucket")

    # The event argument is a dictionary that contains information about the request.
    # This line gets the 'body' field from the event, which in this case is expected to contain a base64-encoded image.
    base64_image = event.get('body', '')

    # The image is then decoded from base64 to get the raw image data.
    image_data = base64.b64decode(base64_image)

    # A unique file name for the image is generated using a UUID, with a '.jpg' extension.
    file_name = f'{uuid.uuid4()}.jpg'   

    # A boto3 S3 client is created, specifying the endpoint URL for localstack.
    s3 = boto3.client('s3', endpoint_url=("http://host.docker.internal:4566"))

    # The name of the S3 bucket where the image will be uploaded is defined.
    bucket_name = "bucket" 

    # The image data is prepared for uploading to S3.
    upload_bucket = BytesIO(image_data)

    # The image is uploaded to S3. If an error occurs during this process, an error message is printed and an HTTP 500 response is returned.
    try:
        s3.upload_fileobj(upload_bucket, bucket_name, file_name)
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': 'Error in uploading image to S3'
        }

    # If the image is uploaded successfully, an HTTP 200 response is returned, with a message indicating the success.
    response = {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*', 
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,PUT,DELETE'
        },
        'body': f'Image {file_name} uploaded to S3 successfully'
    }

    # The response dictionary is returned. AWS Lambda will convert this into an HTTP response.
    return response





def create_bucket_if_not_exists(bucket_name):
    s3_client = boto3.client('s3')
    try:
        s3_client.head_bucket(Bucket=bucket_name)
    except s3_client.exceptions.NoSuchBucket:
        s3_client.create_bucket(Bucket=bucket_name)