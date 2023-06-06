from server.settings import clientOpen
from bson.json_util import dumps, loads
from datetime import datetime

class Explore:
    
    def __init__(self):
        self.client = clientOpen()
        self.page_size = 10

    def rooms(self, page=1):
        # skip = self.page_size * (page - 1)
        skip = page - 1
        res = loads(dumps(self.client.myspace.rooms.find({"live":False}).skip(skip).limit(self.page_size)))
        current_date = str(datetime.utcnow().timestamp())
        new_res = []
        for i in res:
            if current_date>str(i["schedule"]):
                #new_res=[]
                new_res.append(i)
                
        return res

    def liveRooms(self, page=1):
        # skip = self.page_size * (page - 1)
        skip = page - 1
        res = loads(dumps(self.client.myspace.rooms.find({"live":True}).skip(skip).limit(self.page_size)))
        return res
    
    def categoryVideoOld(self, page=1):
        """
        res = {}
        all_categories = loads(dumps(self.client.categories.users.find_one({"id":id})))
        if not all_categories:
            all_categories = loads(dumps(self.client.categories.users.find_one({"_id":"common"})))
            if not all_categories:
                return res

        for i in range(1,16):
            if str(i) not in all_categories["categories"]:
                all_categories.append(str(i))
        videos= loads(dumps(self.client.videos.upload.find()))
        if not videos:
            return res

        for i in all_categories:
            res.update({loads(dumps(self.client.categories.videos.find_one({"_id":i})))["category"]:loads(dumps(self.client.videos.upload.find({"category":i}).sort("timestamp",-1)))[:5]})

        return res
        """
        # skip = self.page_size * (page - 1)
        skip = page - 1
        all_categories = loads(dumps(self.client.categories.video.find()))

        res={}
        for i in all_categories:
            #value = self.client.videos.upload.count({"category":i["_id"]})
            #value = "1.6M Stories"
            #res["total"]=value
            #res.update({i["category"]:value})
            res.update({i["category"]:loads(dumps(self.client.videos.upload.find({"category":i["_id"]}).skip(skip).limit(self.page_size)))})
        return res

    def trendingLiveSpace(self, page: int = 1):
        skip = page - 1
        views = self.client.myspace.rooms.aggregate([
            {
                '$match': {
                    'live': True
                }
            }, {
                '$project': {
                    '_id': 0, 
                    'liveMembers': {
                        '$size': '$allowedUsers'
                    }, 
                    'title': 1, 
                    'description': 1, 
                    'admin': 1, 
                    'room': 1, 
                    'live': 1,
                    'allowedUsers': 1,
                    'streamKey':1,
                    'listeners':1
                }
            }, {
                '$sort': {
                    'liveMembers': -1
                }
            },
            {
                '$skip': skip
            },
            {
                '$limit': self.page_size
            }
        ])
        result = []
        for room in views:
            for user in room["allowedUsers"]:
                if user["email"] == room["admin"]:
                    room["creator"] = user
            result.append(room)
        self.client.close()
        return result
    
    def categoryLiveSpace(self, id, page=1):
        user_category = self.client.categories.users.find_one({"id": id}, {"categories", "sub_cat"})
        if not user_category:
            user_category = self.client.categories.users.find_one({"_id": id}, {"categories", "sub_cat"})
        result = {}
        # start_index = (page - 1) * self.page_size
        start_index = page - 1
        end_index = start_index + self.page_size
        for i in user_category["categories"]:
            category = loads(dumps(self.client.categories.video.find({"_id":i})))
            for j in category:
                rooms = loads(dumps(self.client.myspace.rooms.find({"category":i}).skip(start_index).limit(self.page_size)))
                result.update({j["category"]: rooms})
        return result


    def categoryVideo(self, id, page=1):
        user_categories = self.client.categories.users.find_one({"id": id}, {"categories"})
        result = {}
        # start_index = (page - 1) * self.page_size
        start_index = page - 1
        end_index = start_index + self.page_size
        for i in user_categories["categories"]:
            category = loads(dumps(self.client.categories.video.find({"_id":i})))
            for j in category:
                videos = loads(dumps(self.client.videos.upload.find({"category":i}).skip(start_index).limit(self.page_size)))
                result.update({j["category"]: videos})
        return result


    def topProfiles(self,user_id: str = None, page: int = 1):
        """
        return top profiles
        """
        res=[]
        start_index = page - 1

        try:
            cursor = self.client.auth.profile.find().sort("created_at",-1).skip(start_index).limit(self.page_size)
        except Exception as e:
            # sort by follower
            cursor = self.client.auth.profile.find().sort("follower",-1).skip(start_index).limit(self.page_size)
        for i in cursor:
            if user_id in i['follower']:
                res.append({
                    "_id": i["_id"],
                    "channel_name": i["channel_name"],
                    "name": i["name"],
                    "profile_picture": i["profile_picture"],
                    "area_of_expert":i["area_of_expert"],
                    "followers_data": {
                        "follower": len(i['follower'])
                    },
                    "following_data": {
                        "following": len(i['following'])
                    },
                    "is_following":True
                })
            else:
                res.append({
                    "_id": i["_id"],
                    "channel_name": i["channel_name"],
                    "name": i["name"],
                    "profile_picture": i["profile_picture"],
                    "area_of_expert":i["area_of_expert"],
                    "followers_data": {
                        "follower": len(i['follower'])
                    },
                    "following_data": {
                        "following": len(i['following'])
                    },
                    "is_following":False
                })
        self.client.close()
        return res


    def UserTopProfile(self, user_id, page=1):
        res=[]
        user_profiles = loads(dumps(self.client.auth.profile.find()))
        # start_index = (page - 1) * self.page_size
        start_index = page - 1
        end_index = start_index + self.page_size
        for i in user_profiles:
            if user_id in i["follower"]:
                res.append({
                    "_id": i["_id"],
                    "channel_name": i["channel_name"],
                    "name":i["name"],
                    "profile_picture": i["profile_picture"],
                    "area_of_expert":i["area_of_expert"],
                    "is_following":True
                })
            else:
                res.append({
                    "_id": i["_id"],
                    "channel_name": i["channel_name"],
                    "name": i["name"],
                    "profile_picture": i["profile_picture"],
                    "area_of_expert":i["area_of_expert"],
                    "is_following":False
                })
        self.client.close()
        return res[start_index:end_index]


    def publicEvents(self, page=1):
        
        res=[]
        # start_index = (page - 1) * self.page_size
        start_index = page - 1

        cursor = self.client.explore.images.find().sort("timestamp",-1)
        for i in cursor:
            res.append({
                "id": i["_id"],
                "image_url": i["image"],
                "title": i["title"],
                "description": i["description"],
            })
        self.client.close()
        return res


    def roomRecordings(self, page: int = 1):
        skip = page - 1
        views = self.client.myspace.rooms.aggregate([
            {
                '$match': {
                    'live': False
                }
            }, {
                '$project': {
                    'title': 1, 
                    'admin':1,
                    'creator':1,
                    'room_code':1,
                    'description': 1, 
                    'admin': 1, 
                    'schedule': 1,  
                    'thumbnail': 1,
                    'recordingsFilePath':1
                }
            }, {
                '$sort': {
                    'createdAt': -1
                }
            },
            {
                '$skip': skip
            },
            {
                '$limit': self.page_size
            }
        ])
        # return result
        return list(views)
