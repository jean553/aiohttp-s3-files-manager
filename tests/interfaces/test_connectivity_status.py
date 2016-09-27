import py.test

from client_test import ClientTest

def test_connectivity_status_returns_200():
    client = ClientTest()
    client.get_connectivity_status()
    client.assert_200()
