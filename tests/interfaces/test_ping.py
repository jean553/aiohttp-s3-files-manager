import py.test

from client_test import ClientTest

def test_ping_returns_200():
    client = ClientTest()
    client.get_ping()
    client.assert_200()
