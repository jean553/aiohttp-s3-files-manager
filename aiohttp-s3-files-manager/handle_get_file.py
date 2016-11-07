"""
GET file handler.
"""

import json
import asyncio
import aiobotocore

from aiohttp import web

@asyncio.coroutine
def handle_get_file(request):

    session = aiobotocore.get_session()

    client = session.create_client(
        service_name="s3",
        region_name="",
        aws_secret_access_key="",
        aws_access_key_id="",
        endpoint_url="http://s3:5000"
    )

    response = yield from client.get_object(
        Bucket="mybucket",
        Key="key",
    )

    stream = response["Body"]

    result = web.StreamResponse()
    result.content_type = "application/json"

    yield from result.prepare(request)

    try:
        line = yield from stream.readline()
        fields = line.split(b',')

        while len(line) > 0:
            line = yield from stream.readline()
            values = line.split(b',')

            item = {}
            for index, field in enumerate(fields):
                item[field] = values[index]

            result.write(item)
    finally:
        stream.close()

    yield from result.write_eof()

    client.close()

    return result
