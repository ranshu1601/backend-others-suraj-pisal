from starlette.responses import JSONResponse
from server.auth import jwt_authentication
#from server.settings import notify
from .models import Help


@jwt_authentication
async def sendMessage(request):
    try:
        data = await request.json()

        profile_id = request.user_id

        help = Help()

        help.sendMessage(profile_id, data["user_id"], data["message"])

        return JSONResponse({"message":"Success", "status":True},status_code=200)

    except Exception as e:
        return JSONResponse({"message":str(e), "status":False}, status_code=400)
        

@jwt_authentication 
async def getMessage(request):
    try:
        user_id = request.user_id
        print(user_id)
        help = Help()

        data = help.getMessage(user_id)

        return JSONResponse({"message":data, "status":True},status_code=200)
    except Exception as e:
        return JSONResponse({"message":str(e), "status":False}, status_code=400)   
