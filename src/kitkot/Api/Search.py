


class Search:
    def __init__(self, api):
        self.api = api
        
    def general(self, params={}):
        res = self.api.post_request(path="/search/general", body=params)
        return res
    
    def users(self, params={}):
        res = self.api.post_request(path="/search/users", body=params)
        return res
    
    def videos(self, params={}):
        res = self.api.post_request(path="/search/videos", body=params)
        return res