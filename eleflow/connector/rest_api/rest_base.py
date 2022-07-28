import urllib
import requests
from .spark_rest_response import SparkRestResponse

class Restbase():

    def __init__(self, url_base, api_token_key = None, api_token_value = None, headers = None) -> None:
        """ Initialize the Restbase class.

        Args:
            url_base (str): The base url of the REST API.
            api_token_key (str, optional): Key of the authentication. Defaults to None.
            api_token_value (str, optional): Token bearer. Defaults to None.
            headers (dict, optional): Request headers. Defaults to None.
        """
        self._URL_BASE = url_base
        self._HEADERS = self._get_headers(headers)
        self._API_TOKEN = dict(key=api_token_key, value=api_token_value) if api_token_key and api_token_value else None

    def get(self, *paths, **kwargs) -> SparkRestResponse:
        url = self._build_url(paths, kwargs)
        return SparkRestResponse(url, 'GET', None, self._HEADERS)
        
    def post(self, data, *paths, **kwargs) -> SparkRestResponse:
        url = self._build_url(paths, kwargs)
        return SparkRestResponse(url, 'POST', data, self._HEADERS)
                
    def patch(self, data, *args) -> SparkRestResponse:
        url = self._build_url(*args)
        return SparkRestResponse(url, 'PATCH', data, self._HEADERS)
    
    def put(self, data, *args) -> SparkRestResponse:
        url = self._build_url(*args)
        return SparkRestResponse(url, 'PUT', data, self._HEADERS)

    def delete(self, data=None, *args, **kwargs) -> SparkRestResponse:
        url = self._build_url(*args, **kwargs)
        return SparkRestResponse(url, 'DELETE', data, self._HEADERS)
         
    def _build_url(self, paths, params):
        url = self._build_url_path(paths)
        return self._build_url_query(url, params)
        
    def _build_url_path(self, paths):
        url = self._URL_BASE
        if not url.endswith('/'):
            url += '/'
        if type(paths) is not str and paths and len(paths)>0:
            for path in paths:
                url += path + '/'
        elif len(paths)>0:
            url += paths + '/'
        if url.endswith('/'):
            url = url[:-1]
        return url
    
    def _build_url_query(self, url, params):
        if params and len(params)>0:
            url += '?' + urllib.parse.urlencode(params) + '&'
        else:
            url += '?'
        if self._API_TOKEN:
            url += f'{self._API_TOKEN["key"]}={self._API_TOKEN["value"]}'
        if url.endswith('&'):
            url = url[:-1]
        return url

    def _get_headers(self, headers):
        self._HEADERS = headers
        return self._HEADERS