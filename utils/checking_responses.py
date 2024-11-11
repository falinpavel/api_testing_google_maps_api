"""All methods for checking responses"""
from requests import Response


class CheckingResponses():
    """Methods for checking status code for all requests"""
    @staticmethod
    def check_status_code(response: Response, status_code: int):
        assert status_code == response.status_code
        if status_code == response.status_code:
            print("Test status code PASSED! Fact received status code: " + str(response.status_code))
        else:
            print("Test status code FAILED! Fact received status code: " + str(response.status_code))
