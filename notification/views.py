from server.auth import jwt_authentication, loose_jwt_auth
from starlette.responses import JSONResponse
from .models import Notification

@jwt_authentication
async def notification(request):

    try:

        noti = Notification()

        user_id = request.user_id

        data=await request.json()

        res = noti.addToken(user_id, data['token'])

        noti.close()

        return JSONResponse({"message":res,"status":True})

    except Exception as e:

        return JSONResponse({"message":str(e),"status":False}, status_code=400)

@loose_jwt_auth
async def getUserNotification(request):
    try:
        noti=Notification()
        res = dict()
        res["my_world_notifications"] = [
            {
                'id':'1',
                'username': 'Myworld',
                'profile_image': 'https://my-world-bucket-alpha.s3.ap-south-1.amazonaws.com/notification/72.png',
                'message': 'Welcome to Myworld, To bring your friends on, tap the share icon at the top of the hallway'
            },
            {
                'id':'2',
                'username': 'Myworld',
                'profile_image': 'https://my-world-bucket-alpha.s3.ap-south-1.amazonaws.com/notification/72.png',
                'message': 'We built Myworld to be a more human reality place on the Internet—a world where people solve the problems with help of each other and leave feeling better than when they arrived. Explore the hallways, drop into some hubs, and see what you discover! If you have questions, setting a tab through to view the welcome guide. :) We are so glad you are here!'
            },
        ]
        
        if request.is_authenticated:
            user_id=request.user_id
            res["user_notification"]=noti.getNotification(user_id)
            noti.close()
            
        return JSONResponse({"message":"Success","data":res,"status":True})
    except Exception as e:
        return JSONResponse({"message":str(e),"status":False},status_code=400)
