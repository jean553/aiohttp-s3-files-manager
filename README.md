# aiohttp-s3-files-manager

Simple HTTP service running aiohttp. Used to serve files from S3 bucket using
the streaming method.

## Start the service

```
vagrant up
vagrant ssh
python aiohttp-s3-files-handler/
```

## Create S3 bucket

The S3 bucket creation client uses boto3 which is not compliant with the
botocore version of aibotocore. That's why they are separated in two different
virtual environments.

```
source /tmp/virtual_botoenv/bin/activate
python scripts/create_bucket.py
```

## Tests

```
py.test
```
