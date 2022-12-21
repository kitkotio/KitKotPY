


class Video:
    def __init__(self, api):
        self.api = api
        
    def details(self, params={}):
        res = self.api.get_request(path="/get_user_ids", params=params)
        return res

    def comments(self, params={}):
        res = self.api.get_request(path="/get_user", params=params)
        return res
    
    def comment_replies(self, params={}):
        res = self.api.get_request(path="/get_user/following", params=params)
        return res
    
    def like_comment(self, params={}):
        res = self.api.get_request(path="/get_user/posts", params=params)
        return res
    
    def unlike_comment(self, params={}):
        res = self.api.get_request(path="/get_user/liked_videos", params=params)
        return res