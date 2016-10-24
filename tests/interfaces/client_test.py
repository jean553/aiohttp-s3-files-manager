"""
Simple HTTP client for tests purposes.
"""

from os import getenv
from urllib.parse import urljoin

import requests

class ClientTest(requests.Session):
    """
    Tests purposes routines.
    """

    def __init__(self):
        super(ClientTest, self).__init__()
        self.result = None

    def get_base_url(self):
        """
        Returns the base URL
        """
        host = getenv("HOST", "localhost")
        port = getenv("PORT", "8080")
        return "http://%s:%s" % (host, port)

    def request(
            self,
            method,
            url,
            params=None,
            **kwargs
    ):
        """
        request() method overwritte
        """
        self.result = super(ClientTest, self). request(
            method,
            urljoin(self.get_base_url(), url)
        )
        return self.result

    def get_ping(self):
        self.get("/ping")

    def get_connectivity_status(self):
        self.get("/connectivity-status")

    def get_file(self):
        self.get("/file")

    def assert_200(self):
        assert self.result.status_code == 200, \
            "expected HTTP 200, got %d instead" % self.result.status_code
