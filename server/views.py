from starlette.responses import JSONResponse

async def page_not_found(request):
    return JSONResponse({"message":"404 Page Not Found","status":False}, status_code=404)
