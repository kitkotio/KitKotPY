


class Live:
    def __init__(self, api):
        self.api = api
        
    def feed(self, params={}):
        res = self.api.get_request(path="/live/feed", params=params)
        return res
    
    def join(self, params={}):
        res = self.api.get_request(path="/live/join", params=params)
        return res
    
    def leave(self, params={}):
        res = self.api.get_request(path="/live/leave", params=params)
        return res
    
    def room_exists(self, params={}):
        res = self.api.get_request(path="/live/room_exists", params=params)
        return res
    
    def gifts(self, params={}):
        res = self.api.get_request(path="/live/gifts", params=params)
        return res
    
    def chat(self, params={}):
        res = self.api.get_request(path="/live/chat", params=params)
        return res
    
    def send_message(self, params={}):
        res = self.api.get_request(path="/live/chat/send_message", params=params)
        return res
    
    def get_room_by_user(self, params={}):
        res = self.api.get_request(path="/live/chat/send_message", params=params)
        return res