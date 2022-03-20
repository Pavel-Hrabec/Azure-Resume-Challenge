import unittest

import azure.functions as func
from second_function.Function import main

class TestFunction(unittest.TestCase):
    def test_second_function(self):
        # Construct a mock HTTP request
        req = func.HttpRequest(
            method='GET',
            body=None,
            url='/api/second_function',
            params={'value': '21'})

        # Call the function
        resp = main(req)

        # Check the output
        self.assertEqual(
            resp.get_body(),
            b'21 * 2 = 42',
        )