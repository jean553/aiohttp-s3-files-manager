"""
Starting point of the service.
"""

from aiohttp import web

from handle_get_ping import handle_get_ping

def main():
    """
    Starts the service.
    """

    app = web.Application()
    app.router.add_get('/ping', handle_get_ping)
    web.run_app(app)

if __name__ == "__main__":
    main()
