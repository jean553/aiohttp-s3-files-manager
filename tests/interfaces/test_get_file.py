import py.test

from client_test import ClientTest

def test_file_returns_200():
    client = ClientTest()
    client.get_file()
    client.assert_200()
