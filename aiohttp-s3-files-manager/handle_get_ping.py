"""
GET ping handler.
"""

from aiohttp import web

async def handle_get_ping(request):
    return web.Response(text="OK")
