#!/usr/bin/python
'''
Creates a dummy bucket inside the S3 fake service.
'''

import os
import boto3

def generate_bucket():
    '''
    Generate the bucket according
    to the environment variables
    '''

    resource = boto3.resource(
        service_name='s3',
        aws_access_key_id='',
        aws_secret_access_key='',
        endpoint_url=os.getenv('S3_ENDPOINT')
    )

    resource.create_bucket(Bucket=os.getenv('BUCKET_NAME'))

def main():
    '''
    Script entry point
    '''
    generate_bucket()

if __name__ == '__main__':
    main()
