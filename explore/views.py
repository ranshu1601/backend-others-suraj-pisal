from server.auth import loose_jwt_auth, jwt_authentication
from starlette.responses import JSONResponse
from .models import Explore
from starlette.responses import Response
from bson.json_util import dumps, loads
import json



def parse_json(data):
    """function to parse data as a json"""
    return json.loads(dumps(data))


@loose_jwt_auth
async def explore(request):

    #import pdb; pdb.set_trace();

    try:
        try:
    
            data = await request.json()
            page = data['page']
            
            if page is None:
                page = 1
        except:
            page = 1
        
        exp = Explore()

        res = dict()

        try:

            res["public_events"]=exp.publicEvents(page)
        except Exception as e:
            res["public_events"]=[]

        try:
            res["rooms"]=exp.rooms(page)
        except Exception as e:
            res["rooms"]=[]
        try:
            res["live_rooms"]=exp.liveRooms(page)
        except Exception as e:
            res["live_rooms"]=[]
        
        
        # res["top_profiles"]=exp.topProfiles()
        res["videos"]=exp.categoryVideoOld(page)

        if request.is_authenticated:
            
            user_id = request.user_id
            try:
                res["top_profiles"]=exp.UserTopProfile(user_id=user_id, page=page)
            except Exception as e:
                res["top_profiles"]=[]

        else:
            try:
                res["top_profiles"] = exp.topProfiles(user_id,page=page)
            except Exception as e:
                res["top_profiles"] = []
            
#         parse data as a json
        res = parse_json(res)
        return JSONResponse({"message":res,"status":True})

    except Exception as e:
        print('expecepition')
        return JSONResponse({"message":str(e),"status":False}, status_code=400)


async def publicEvents(request):
    try:
        exp = Explore()
        res = dict()
        try:
            data = await request.json()
            page = data['page']
            if page is None:
                page = 1
            res['public_events'] = exp.publicEvents(page)
        except Exception as e:
            res['public_events'] = []
        res = parse_json(res)
        return JSONResponse({"message": res, "status":True})
    except Exception as e:
        return JSONResponse({"message": str(e), "status": False}, status_code=400)

async def rooms(request):
    try:
        exp = Explore()
        res = dict()
        try:
            # data = await request.json()
            page = request.path_params['page']
            if page is None:
                page = 1
            res['rooms'] = exp.rooms(page)
        except Exception as e:
            res['rooms'] = []
        res = parse_json(res)
        return JSONResponse({"message": res, "status":True})
    except Exception as e:
        return JSONResponse({"message": str(e), "status": False}, status_code=400)

async def liveRooms(request):
    try:
        exp = Explore()
        res = dict()
        try:
            data = await request.json()
            page = data['page']
            if page is None:
                page = 1
            res['live_rooms'] = exp.liveRooms(page)
        except Exception as e:
            res['live_rooms'] = []
        res = parse_json(res)
        return JSONResponse({"message": res, "status":True})
    except Exception as e:
        return JSONResponse({"message": str(e), "status": False}, status_code=400)

@loose_jwt_auth
async def topProfiles(request):
    print('hello')
    try:
        exp = Explore()
        res = dict()
        try:
            # get page 
            page = request.path_params['page']
            if page is None:
                page = 1
            if request.is_authenticated:
                user_id = request.user_id
                res['top_profiles'] = exp.UserTopProfile(user_id=user_id, page=page)
            res['top_profiles'] = exp.topProfiles(page)
        except Exception as e:
            res['top_profiles'] = []
        res = parse_json(res)
        return JSONResponse({"message": res, "status":True})
    except Exception as e:
        print('hello')
        return JSONResponse({"message": str(e), "status": False}, status_code=400)

async def UserTopProfile(request):
    try:
        exp = Explore()
        res = dict()
        try:
            # data = await request.json()
            page = request.path_params['page']
            if page is None:
                page = 1
            user_id = request.path_params["user_id"]
            res['top_profiles'] = exp.UserTopProfile(user_id=user_id, page=page)
        except Exception as e:
            res['top_profiles'] = []
        res = parse_json(res)
        return JSONResponse({"message": res, "status":True})
    except Exception as e:
        return JSONResponse({"message": str(e), "status": False}, status_code=400)

async def categoryVideoOld(request):
    try:
        exp = Explore()
        res = dict()
        try:
            data = await request.json()
            page = data['page']
            if page is None:
                page = 1
            res['videos'] = exp.categoryVideoOld(page)
        except Exception as e:
            res['videos'] = []
        res = parse_json(res)
        return JSONResponse({"message": res, "status":True})
    except Exception as e:
        return JSONResponse({"message": str(e), "status": False}, status_code=400)


async def exploreVideo(request):
    try:
        exp = Explore()
        try:
    
            # data = await request.json()
            page = request.path_params['page']
            
            if page <= 0:
                page = 1
        except:
            page = 1
        id = request.path_params["user_id"]
        try:
            res = exp.categoryVideo(id=id, page=page)
            res = parse_json(res)
    
            return JSONResponse({"message": res, "status":True})
        except Exception as e:
            return JSONResponse(
                {'message':[],'status':False},status_code=404
            )
    except Exception as e:
        return JSONResponse({"message": [],"status": False}, status_code=400)
    

async def trendingLiveSpace(request):
    print('trending')
    try:
        exp = Explore()
        
        page = request.path_params['page']
        if page is None:
            page = 1
        res = exp.trendingLiveSpace(page=page)
        res = parse_json(res)
        return JSONResponse({"message": res, "status":True}) 
    # instead of sending message as string send it as a empty list(frontend requirement)
    
        
    except Exception as e:
        return JSONResponse({"message": str(e), "status": False}, status_code=400)
        

async def exploreLiveSpaceCategory(request):
    try:
        exp = Explore()
        try:
    
            # data = await request.json()
            page = request.path_params['page']
            
            if page <= 0:
                page = 1
        except:
            page = 1
        id = request.path_params["user_id"]
        res = exp.categoryLiveSpace(id=id,page=page)
        res = parse_json(res)    # parse data as a json
        return JSONResponse({"message": res, "status":True})
    except Exception as e:
        return JSONResponse({"message": str(e), "status": False}, status_code=400)

async def roomRecordings(request):
    try:
        exp = Explore()
        res = dict()
        page = request.path_params['page']
        res['Technology'] = exp.roomRecordings(page)
        res = parse_json(res)
        return JSONResponse({"message": res, "status":True})
    except Exception as e:
        return JSONResponse({"message": str(e), "status": False}, status_code=400)
