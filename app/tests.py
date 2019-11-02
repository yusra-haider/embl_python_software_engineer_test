# core module
import unittest

# python libraries
import requests

VALIDATION_ERROR = 400
SUCCESS = 200
INVALID_REQUEST_METHOD = 405
# this is the url on which the server runs inside docker
BASE_URL = "http://0.0.0.0:80"


# ideally I would have wanted to use a separate, dedicated testdb to do data driven
# testing with the setUp, tearDown functions in unittest, by
# using this super cool library called testcontainers (https://github.com/testcontainers/testcontainers-python)
# testcontainers allows us to generate testcontainers on the fly, programmatically

# for this I would have to use environment variables to define the test and dev/prod envs

# doing so would have given better, more accurate and controlled tests

class GeneSearchEndPointTest(unittest.TestCase):
    end_point = "{}/gene_search/".format(BASE_URL)

    def test_required_param_name(self):
        # checking that gene_search won't work without specifying
        # the required param 'name'
        response = requests.get(self.end_point)
        self.assertEqual(response.status_code, VALIDATION_ERROR)

    def test_invalid_length_param_name(self):
        # test that gene_search fails if name value length is in range [1,2]
        params = [{"name": "a"}, {"name": "ab"}]

        for param in params:
            with self.subTest(param=param):
                response = requests.get(self.end_point, param)
                self.assertEqual(response.status_code, VALIDATION_ERROR)

    def test_required_and_valid_length_param_name(self):
        # test that gene_search gives successful result
        # as soon as the name param is specified and has the right length (3)
        response = requests.get(self.end_point,
                                params={"name": "abc"})
        self.assertEqual(response.status_code, SUCCESS)

    def test_invalid_request_method(self):
        # test that gene_search fails for the request methods defined below
        request_methods = [requests.post, requests.put, requests.patch, requests.delete]
        for request_method in request_methods:
            with self.subTest(request_method=request_method):
                response = request_method(self.end_point)
                self.assertEqual(response.status_code, INVALID_REQUEST_METHOD)


if __name__ == '__main__':
    # add option for args here so that BASE_URL can be configured
    unittest.main(verbosity=2)

