# core module
import argparse
import unittest

# python libraries
import requests

VALIDATION_ERROR = 400
SUCCESS = 200
INVALID_REQUEST_METHOD = 405
WEB_SERVER_URL = "http://0.0.0.0:80"


# ideally I would have wanted to use a separate, dedicated testdb to do data driven
# testing with the setUp, tearDown functions in unittest, by
# using this super cool library called testcontainers (https://github.com/testcontainers/testcontainers-python)
# testcontainers allows us to generate testcontainers on the fly, programmatically

# for this I would have to use environment variables to define the test and dev/prod envs

# doing so would have given better, more accurate and controlled tests

class GeneSearchEndPointTest(unittest.TestCase):
    end_point = "{}/gene_search/".format(WEB_SERVER_URL)

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

    def test_invalid_request_method(self):
        # test that gene_search fails for the request methods defined below
        request_methods = [requests.post, requests.put, requests.patch, requests.delete]
        for request_method in request_methods:
            with self.subTest(request_method=request_method):
                response = request_method(self.end_point)
                self.assertEqual(response.status_code, INVALID_REQUEST_METHOD)

    def test_required_and_valid_length_param_name(self):
        # test that gene_search gives successful result
        # as soon as the name param is specified and has the right length (3)
        response = requests.get(self.end_point,
                                params={"name": "abc"})
        self.assertEqual(response.status_code, SUCCESS)

    # note that these tests aren't entirely accurate;
    # they would be if the test db was entirely deterministic
    # and under the test suite control
    def test_result_validity(self):
        params = [{"name": "abc", "species": "amphilophus_citrinellus"},
                  {"name": "abc", "species": "amphilophus_citrinellus", "limit": 50}]
        for param in params:
            with self.subTest(param=param):
                response = requests.get(self.end_point, param)
                self.assertEqual(response.status_code, SUCCESS)
                elems = response.json()
                self.assertLessEqual(len(elems), param.get("limit", 10))  # because 10 is the default limit value
                # adding more tests that check the actual data..
                self.assertTrue(all([elem["name"].lower().startswith(param["name"]) for elem in elems]))
                self.assertTrue(all([elem["species"] == param["species"] for elem in elems]))


if __name__ == '__main__':
    # add option for args here so that BASE_URL can be configured
    parser = argparse.ArgumentParser()
    parser.add_argument("-add","--address", help="address of web server under test. "
                                                 "Required format: 'http://<host>:<ip>'")
    args = parser.parse_args()
    WEB_SERVER_URL = args.address if args.address else "http://0.0.0.0:80"
    unittest.main(verbosity=2)

