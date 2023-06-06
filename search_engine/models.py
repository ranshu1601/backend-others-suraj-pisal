from server.settings import clientOpen
from bson.json_util import dumps, loads
import json

class SearchEngine:

    def __init__(self):
        self.client = clientOpen()

    def searchPublicProfile(self, name):
    
        res=[]

        for i in loads(dumps(self.client.auth.profile.find({
            "channel_name":{"$regex":name, "$options":"i"}
        }).sort("name",1))):
            res.append(
                {
                    "_id":i["_id"],
                    "name":i["name"],
                    "channel_name":i["channel_name"],
                    "profile_picture":i["profile_picture"]
                }
            )

        return res

    def searchVideo(self, name):

        res = loads(dumps(self.client.videos.upload.find({"title":{"$regex":name, "$options":"i"}}).sort("timestamp",-1)))
        return res


    def searchMyspace(self, name):
        res = loads(dumps(self.client.myspace.rooms.find({"title":{"$regex":name, "$options":"i"}})))
        res = json.loads(dumps(res))
        return res
        
 
    def close(self):
        self.client.close()

