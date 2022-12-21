


class User:
    def __init__(self, api):
        self.api = api
        
    def get_user_ids(self, params={}):
        res = self.api.get_request(path="/get_user_ids", params=params)
        return res

    def get_user(self, params={}):
        res = self.api.get_request(path="/get_user", params=params)
        return res
    
    def get_following(self, params={}):
        res = self.api.get_request(path="/get_user/following", params=params)
        return res
    
    def get_posts(self, params={}):
        res = self.api.get_request(path="/get_user/posts", params=params)
        return res
    
    def liked_videos(self, params={}):
        res = self.api.get_request(path="/get_user/liked_videos", params=params)
        return res
    
    def get_story(self, params={}):
        res = self.api.get_request(path="/get_user/story", params=params)
        return res
        
    def get_followers(self, params={}):
        res = self.api.get_request(path="/get_user/followers", params=params)
        return res