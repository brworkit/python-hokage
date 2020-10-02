import boto3
import ast
import jwt

from botocore.exceptions import ClientError

DEFAULTS = {
        'verify_signature': False,
        'verify_aud': False,
        'verify_iat': False,
        'verify_exp': False,
        'verify_nbf': False,
        'verify_iss': False,
        'verify_sub': False,
        'verify_jti': False,
        'verify_at_hash': False,
        'leeway': 0}

def get_app_client(authorization):
    return jwt.decode(authorization, algorithms=['RS256'], options=DEFAULTS)['client_id']

def get_secrets(region, secret):
    try:
        session = boto3.session.Session()
        client = session.client(service_name='secretsmanager', region_name=region)
        response = client.get_secret_value(SecretId=secret)
        return ast.literal_eval(response['SecretString'])
    except ClientError as e:
        raise e

def get_issuer(region, authorization):
    return get_secrets(region=region, secret=get_app_client(authorization))