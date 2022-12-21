


class Music:
    def __init__(self, api):
        self.api = api
        
    def search(self, params={}):
        res = self.api.get_request(path="/music/search", params=params)
        return res