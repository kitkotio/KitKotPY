import requests

from Api.Account import Account
from Api.Music import Music
from Api.Search import Search
from Api.User import User
from Api.Video import Video

class KitKot:
    def __init__(self, api_key, session_key=None):
        self.api_key = api_key
        self.session_key = session_key
        self.baseURL = "https://kitkot.xyz/api"
        self.baseParams = {
            "api_key": api_key
        }
        if self.session_key:
            self.baseParams["session_key"] = self.session_key
            
        self.account = Account(self)
        self.user = User(self)
        self.search = Search(self)
        self.video = Video(self)
        self.music = Music(self)

    def get_request(self, path, params={}):
        req = requests.get(f"{self.baseURL}{path}", params=self.merge_dicts(self.baseParams, params))
        res = req.json()
        return res
    
    def post_request(self, path, params={}, body={}):
        req = requests.post(f"{self.baseURL}{path}", params=self.merge_dicts(self.baseParams, params), headers={'content-type': 'application/json'}, json=body)
        res = req.json()
        return res
    
    def get_session(self, params={}):
        res = self.get_request(path="/session", params=params)
        return res
    
    def get_sessions(self):
        res = self.get_request(path="/sessions")
        return res
    
    def merge_dicts(self, d1, d2):
        d = d1.copy()
        d.update(d2)
        return d