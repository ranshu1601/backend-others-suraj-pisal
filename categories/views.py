from server.auth import jwt_authentication
from starlette.responses import JSONResponse
from .models import MusicCategoriesUpload, VideoCategoriesUpload


async def videoCategories(request):

    try:

        category = VideoCategoriesUpload()

        if request.method=="POST":
            
            data = await request.json()

            category.create(data["id"], data["category"])
            
            return JSONResponse({"message":"Category Created","status":True})

        return JSONResponse({"message":"Success","data":category.get(),"status":True})

    except Exception as e:

        return JSONResponse({"message":str(e),"status":False}, status_code=400)

async def subCategories(request):
    try:
        category = VideoCategoriesUpload()
        print(request.method)
        if request.method == "POST":
            data = await request.json()
            category.addSubCat(data["sub_cat_id"], data["category_id"], data["sub_category"])
            return JSONResponse({"message": "Sub Category Created", "status":True})

        elif request.method == "GET":
            return JSONResponse({"message":"Success","data":category.getSubCat(),"status":True})  

    except Exception as e:

        return JSONResponse({"message": str(e), "status":False}, status_code=400)

          
          
async def musicCategories(request):
    print("music category")
    try:

        category = MusicCategoriesUpload()

        if request.method=="POST":
            
            data = await request.json()

            category.create(data["id"],data["category"])

            return JSONResponse({"message":"Category Created","status":True})

        return JSONResponse({"message":"Success","data":category.get(),"status":True})

    except Exception as e:

        return JSONResponse({"message":str(e),"status":False}, status_code=400)

@jwt_authentication
async def authenticatedCategory(request):

    try:
        data = await request.json()

        user_id = request.user_id

        category = VideoCategoriesUpload()

        category.auth(data['device_id'],user_id)

        return JSONResponse({"message":"Success", "status":True}, status_code=200)

    except Exception as e:
        return JSONResponse({"message":str(e), "status":False}, status_code=400)

async def getUserCategories(request):
    
    try:
        data = await request.json()

        category = VideoCategoriesUpload()

        category.getUserCat(data['device_id'],data['categories'], data['sub_categories'])

        return JSONResponse({"message":"Success", "status":True}, status_code=200)

    except Exception as e:
        return JSONResponse({"message":str(e), "status":False}, status_code=400)

