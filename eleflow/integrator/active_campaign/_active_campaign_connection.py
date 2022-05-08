from _active_campaign_service_client import ActiveCampaignServiceClient

class ActiveCampaingConnection():

    def __init__(self, token_api, account_name) -> None:
        self._TOKEN_API = token_api
        self._BASE_URL = f"https://{account_name}.api-us1.com/api/3/" 

    @classmethod
    def v1_from_token_api(cls, token_api, account_name):
        return cls(
            token_api, 
            account_name
        )

    def get_service_client(self):
        return ActiveCampaignServiceClient(self._TOKEN_API, self._BASE_URL)