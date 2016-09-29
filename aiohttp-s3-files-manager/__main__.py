"""
Starting point of the service.
"""

from aiohttp import web

from handle_get_ping import handle_get_ping
from handle_get_connectivity_status import handle_get_connectivity_status
from handle_get_file import handle_get_file

def main():
    """
    Starts the service.
    """

    app = web.Application()
    app.router.add_get('/ping', handle_get_ping)
    app.router.add_get('/connectivity-status', handle_get_connectivity_status)
    app.router.add_get('/file', handle_get_file)
    web.run_app(app)

if __name__ == "__main__":
    main()
