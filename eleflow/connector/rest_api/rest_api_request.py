from rest_base import Restbase

class RestApiRequest(Restbase):
    
    @classmethod
    def build(cls, url_base, api_token_key = None, api_token_value = None, headers = None) -> None:
        return cls(url_base, api_token_key, api_token_value, headers)