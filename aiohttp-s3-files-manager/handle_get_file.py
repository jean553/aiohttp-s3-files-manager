"""
GET file handler.
"""

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
    result.content_type = "text/plain"

    yield from result.prepare(request)

    try:
        line = yield from stream.readline()
        result.write(line)

        while len(line) > 0:
            line = yield from stream.readline()
            result.write(line)
    finally:
        stream.close()

    yield from result.write_eof()

    client.close()

    return result
