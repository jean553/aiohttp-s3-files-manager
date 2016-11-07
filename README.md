# aiohttp-s3-files-manager

Simple HTTP service running aiohttp. Used to serve files from S3 bucket using
the streaming method.

## Start the service

```
vagrant up
vagrant ssh
python aiohttp-s3-files-manager
```

## Create S3 bucket

The S3 bucket creation client uses boto3 which is not compliant with the
botocore version of aibotocore. That's why they are separated in two different
virtual environments.

```
source /tmp/virtual_botoenv/bin/activate
python scripts/create_bucket.py
```

## Upload file into the created bucket

```
curl "http://s3:5000/mybucket/1?AWSAccessKeyId=dummy_value&Expires=1475162584&Signature=dummy_signature" --upload-file file.csv
```

## Tests

```
py.test
```
