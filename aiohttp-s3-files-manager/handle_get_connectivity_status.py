"""
GET connectivity status handler.
"""

import asyncio
import aiobotocore

from aiohttp import web

@asyncio.coroutine
def handle_get_connectivity_status(loop):

    session = aiobotocore.get_session(loop=loop)

    client = session.create_client(
        service_name="s3",
        region_name="",
        aws_secret_access_key="",
        aws_access_key_id="",
        endpoint_url="http://s3:5000"
    )

    response = yield from client.put_object(
        Bucket="mybucket",
        Key="key",
        Body="data"
    )

    return web.Response(text="OK")
