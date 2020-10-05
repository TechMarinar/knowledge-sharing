import boto3
import sys

def get_pool_credentials(region, identity_pool):
    client = boto3.client('cognito-identity', region_name=region)

    _id = client.get_id(IdentityPoolId=identity_pool)
    _id = _id['IdentityId']

    credentials = client.get_credentials_for_identity(IdentityId=_id)
    access_key = credentials['Credentials']['AccessKeyId']
    secret_key = credentials['Credentials']['SecretKey']
    session_token = credentials['Credentials']['SessionToken']
    identity_id = credentials['IdentityId']

    print ("Access Key: " + access_key + "\n")
    print ("Secret Key: " + secret_key + "\n") 
    print ("Session Token: " + session_token + "\n")
    print ("Identity ID: " + identity_id + "\n")

get_pool_credentials(sys.argv[1], sys.argv[2]);