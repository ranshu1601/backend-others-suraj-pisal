from server.settings import clientOpen
from bson.json_util import dumps, loads

class Notification:

    def __init__(self):
        self.client = clientOpen()

    def addToken(self, profile, token):
        
        if self.client.notifications.tokens.find_one({"profile":profile}):
            self.client.notifications.tokens.update({"profile":profile},{
                "profile":profile,
                "token":token
            })

            return "Token Updated"
    
        self.client.notifications.tokens.insert_one({
            "profile":profile,
            "token":token
        })
        
        return "Token Added"

    def getNotification(self, user_id):
        return self.client.notifications.notification.find_one({"id":user_id})
        
    def close(self):
        self.client.close()
