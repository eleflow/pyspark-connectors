import requests
import urllib

from rest_api._spark_rest_response import SparkRestResponse

class Restbase():

    def __init__(self, url_base,api_token_key, api_token_value) -> None:
        self._URL_BASE = url_base
        self._API_TOKEN = api_token

    def get(self, *paths, **kwargs) -> SparkRestResponse:
        url = self._build_url(paths, kwargs)
        return SparkRestResponse(requests.get(url))
        
    def post(self, data, *paths, **kwargs) -> SparkRestResponse:
        url = self._build_url(paths, kwargs)
        return SparkRestResponse(requests.post(url, data=data))
        
    def patch(self, data, *args) -> SparkRestResponse:
        url = self._build_url(*args)
        return SparkRestResponse(requests.patch(url, data=data))
    
    def put(self, data, *args) -> SparkRestResponse:
        url = self._build_url(*args)
        return SparkRestResponse(requests.put(url, data=data))

    def delete(self, data=None, *args, **kwargs) -> SparkRestResponse:
        url = self._build_url(*args, **kwargs)
        return SparkRestResponse(requests.delete(url, data=data))
         
    def _build_url(self, paths, params):
        url = self._build_url_path(paths)
        return self._build_url_query(url, params)
        
    def _build_url_path(self, paths):
        url = self._URL_BASE
        if paths and len(paths)>0:
            for path in paths:
                url += path + '/'
        return url
    
    def _build_url_query(self, url, params):
        if params and len(params)>0:
            url += '?' + urllib.parse.urlencode(params) + '&'
        else:
            url += '?'
        url += f'api_token={self._API_TOKEN}'
        return url