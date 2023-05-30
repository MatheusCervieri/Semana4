from io import BytesIO
import json
import base64
import boto3
import uuid

def post_handler(event, context):
    print("Olá, nos estamos usando o S3 dentro do localstack, por isso, você precisa criar um bucket no seu localstack com o nome bucket")
    # get the base64-encoded body
    base64_image = event.get('body', '')

    # decode the image
    image_data = base64.b64decode(base64_image)
    file_name = f'{uuid.uuid4()}.jpg'   

    # Connect to the s3 localstack
    print("Teste aleatório")
    print("Chegou aqui!!!")
    s3 = boto3.client('s3', endpoint_url=("http://host.docker.internal:4566"))
    bucket_name = "bucket" # replace with your bucket name
    print("O s3 foi criado com sucesso")
    # Upload the file
    upload_bucket = BytesIO(image_data)
    print("Chegou aqui")
    try:
        s3.upload_fileobj(upload_bucket, bucket_name, file_name)
        print("Put object")
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': 'Error in uploading image to S3'
        }

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




def create_bucket_if_not_exists(bucket_name):
    s3_client = boto3.client('s3')
    try:
        s3_client.head_bucket(Bucket=bucket_name)
    except s3_client.exceptions.NoSuchBucket:
        s3_client.create_bucket(Bucket=bucket_name)