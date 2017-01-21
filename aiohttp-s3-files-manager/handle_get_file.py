"""
GET file handler.
"""

import json
import asyncio
import aiobotocore

from aiohttp import web

UTF8 = "utf-8"

@asyncio.coroutine
def handle_get_file(request):

    session = aiobotocore.get_session()

    client = session.create_client(
        service_name="s3",
        region_name="",
        aws_secret_access_key="",
        aws_access_key_id="",
        endpoint_url="http://s3:5000",
    )

    response = yield from client.get_object(
        Bucket="mybucket",
        Key="Key",
    )

    stream = response["Body"]

    result = web.StreamResponse()
    result.content_type = "application/json"

    yield from result.prepare(request)

    result.write(b'{[')

    try:
        line = yield from stream.readline()
        fields = line.split(b',')

        line = yield from stream.readline()

        while len(line) > 0:

            values = line.split(b',')

            item = {}
            for index, field in enumerate(fields):
                field = field.decode(UTF8).replace('\n', '')
                value = values[index].decode(UTF8).replace('\n', '')
                item[field] = value

            line = yield from stream.readline()

            response = json.dumps(item)

            if len(line) > 0:
                response += ","

            result.write(response.encode())

        result.write(b']}')

    finally:
        stream.close()

    yield from result.write_eof()

    client.close()

    return result
