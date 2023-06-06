from boto3 import client
from server.settings import clientOpen
from bson.json_util import dumps, loads
from datetime import datetime

class MusicUpload:

    def __init__(self):    
        self.client = clientOpen()

    def create(self, title, thumbnail, duration, category, upload_file):
        
        self.client.music.upload.insert_one({
            "_id":title+"_"+str(datetime.utcnow().timestamp())+"_"+duration,
            "title":title,
            "thumbnail":thumbnail,
            "duration":duration,
            "category":category,
            "upload_file":upload_file
        })
        self.client.close()

    def get(self):
        # loads(dumps(client.music.upload.find()))

        all_categories = loads(dumps(self.client.categories.music.find()))

        res = {}

        for i in all_categories:
            res.update({i["category"]:loads(dumps(self.client.music.upload.find({"category":i["_id"]})))})

        self.client.close()

        return res

