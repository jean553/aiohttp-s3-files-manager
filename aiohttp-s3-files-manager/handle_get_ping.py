'''GET ping handler.
'''

import asyncio

from aiohttp import web

@asyncio.coroutine
def handle_get_ping(request):
    return web.Response(text='OK')
