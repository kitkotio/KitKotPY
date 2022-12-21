


class Account:
    def __init__(self, api):
        self.api = api
        
    def login(self, params={}):
        res = self.api.get_request(path="/login", params=params)
        return res
    
    def me(self):
        res = self.api.get_request(path="/get_me")
        return res
    
    def edit(self, params={}):
        res = self.api.get_request(path="/profile/edit", params=params)
        return res
    
    def fyp(self, params={}):
        res = self.api.get_request(path="/get_user/feed", params=params)
        return res
    
    def comment(self, params={}):
        res = self.api.get_request(path="/video/comments/publish", params=params)
        return res
    
    def comment_reply(self, params={}):
        res = self.api.get_request(path="/video/comments/publish/reply", params=params)
        return res
    
    def delete_comment(self, params={}):
        res = self.api.get_request(path="/video/comments/delete", params=params)
        return res
    
    def inbox(self, params={}):
        res = self.api.get_request(path="/profile/inbox", params=params)
        return res
    
    def like_video(self, params={}):
        res = self.api.get_request(path="/video/like", params=params)
        return res
    
    def unlike_video(self, params={}):
        res = self.api.get_request(path="/video/unlike", params=params)
        return res
    
    def follow_user(self, params={}):
        res = self.api.get_request(path="/profile/follow", params=params)
        return res
    
    def unfollow_user(self, params={}):
        res = self.api.get_request(path="/profile/unfollow", params=params)
        return res