import json 

def get_handler(event, context):

    response = {
        'statusCode': 200,
        'body': json.dumps({'file_url': file_url})
    }
    return response