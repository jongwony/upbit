import os

import boto3

ssm = boto3.client('ssm')


def get_parameter(name, with_decryption=True):
    response = ssm.get_parameter(Name=name, WithDecryption=with_decryption)
    return response['Parameter']['Value']


def server_api(path):
    return server_uri + path


access_key = get_parameter('/api_key/upbit/access_key')
secret_key = get_parameter('/api_key/upbit/secret_key')
server_uri = 'https://api.upbit.com'

os.environ['UPBIT_OPEN_API_ACCESS_KEY'] = access_key
os.environ['UPBIT_OPEN_API_SECRET_KEY'] = secret_key
os.environ['UPBIT_OPEN_API_SERVER_URI'] = server_uri
