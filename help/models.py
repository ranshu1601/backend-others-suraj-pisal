from bson.json_util import dumps, loads
from server.settings import clientOpen
from datetime import datetime


class Help:

    def __init__(self):
        self.client=clientOpen()

    def sendMessage(self, profile_id, user_id, message):
        user_profile = self.client.auth.profile.find_one({"_id":profile_id})
        profile_picture=user_profile["profile_picture"]

        self.client.help.message.insert_one({
            "_id":user_id+"_"+str(datetime.utcnow().timestamp()),
            "sender_id":profile_id,
            "profile_picture":profile_picture,
            "receiver_id":user_id,
            "message":message,
            "time":str(datetime.utcnow().timestamp()),
            "seen":False,
        })
        return "Message Send"

    def getMessage(self,user_id):

        res = loads(dumps(self.client.help.message.find({"receiver_id":user_id})))

        return res
        