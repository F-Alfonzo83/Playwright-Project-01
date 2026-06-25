from playwright.sync_api import Playwright
from configurations.config import Config

class BaseClient:
    def __init__(self,playwright: Playwright, timeout:float=15_000.):
        '''
        BaseClient() Initializator
        Args:
            playwright: Playwright: Instance of Playwrightq
            base_url: str: Base URL for the Requests
            timeout: float:=10: Request Timeout in Seconds
        '''
        config = Config()
        self.playwright = playwright
        self.base_url = config.get_api_baseurl()
        self.timeout = timeout
        self.headers = {"Content-Type": "application/json"}

        self._request = playwright.request.new_context(base_url=self.base_url,
                                                       timeout=self.timeout)

    def _get(self, url: str=None, headers:dict=None, **kwargs):
        request_headers = self.headers.copy()
        if headers is not None:
            request_headers.update(headers)

        response = self._request.get(url=url,
                                     headers=request_headers,
                                     **kwargs)
        return response

    def _post(self, url: str,data:dict, headers:dict=None, **kwargs):
        request_headers = self.headers.copy()
        if headers is not None:
            request_headers.update(headers)
        response = self._request.post(url=url,
                                      headers=request_headers,
                                      data=data)
        return response


