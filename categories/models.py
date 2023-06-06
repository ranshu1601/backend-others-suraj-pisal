from server.settings import clientOpen
from bson.json_util import dumps, loads

class MusicCategoriesUpload:

    def __init__(self):
        self.client = clientOpen()

    def create(self, id, category):

        self.client.categories.music.insert_one({
            "_id":id,
            "category":category,
        })
        self.client.close()

    def get(self):

        res = loads(dumps(self.client.categories.music.find()))
        self.client.close()
        return res

class VideoCategoriesUpload:

    def __init__(self):
        self.client = clientOpen()
    
    def create(self, id, category):

        self.client.categories.video.insert_one({
            "_id":id,
            "category":category,
        })
        self.client.close()

    def addSubCat(self, sub_cat_id, category_id, sub_category):
        self.client.categories.subcategories.insert_one({
            "_id": category_id+"_"+sub_cat_id,
            "id": sub_cat_id,
            "category_id": category_id,
            "sub_category": sub_category,
        })
        self.client.close()

    def getSubCat(self):
        all_categories = loads(dumps(self.client.categories.video.find()))

        res = {}
        for i in all_categories:
            res.update({i["category"]:loads(dumps(self.client.categories.subcategories.find({"category_id": i["_id"]},{"_id","category_id","sub_category"})))})

        self.client.close()
        return res
                            

    def getUserCat(self, device_id, category, sub_category):
        # import pdb; pdb.set_trace();

        if self.client.categories.users.find_one({"_id":device_id}):
            self.client.categories.users.update({"_id":device_id},{
                "$set":{
                    "categories":category,
                    "sub_category":sub_category
                }
            })
        
        else:
            self.client.categories.users.insert_one({
                "_id":device_id,
                "id":device_id,
                "categories":category,
                "sub_cat": sub_category,
            })
        self.client.close()
        

    def get(self):
        
        res = loads(dumps(self.client.categories.video.find()))
        self.client.close()
        return res


    def auth(self, device_id, user_id):
        self.client.categories.users.update_one({"id":device_id}, { "$set": { "id": user_id, "_id": user_id } })
        self.client.close()

