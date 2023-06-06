from music.models import MusicUpload
from starlette.responses import JSONResponse
from server.settings import s3Client, AWS_STORAGE_BUCKET_NAME, AWS_BASE_URL
from os import system
from datetime import datetime

async def postMusic(request):
    try:
        form = await request.form()

        music = form["thumbnail"]

        th_file_name = f"media/Music_Thumbnail/music{str(int(datetime.utcnow().timestamp()))}.jpg"

        with open(th_file_name,"wb+") as f:
            f.write(await music.read())

        s3 = s3Client()
        s3.upload_file(
            th_file_name,
            AWS_STORAGE_BUCKET_NAME,
            th_file_name[6:],
            ExtraArgs={"ACL": "public-read"}
        )

        music = form["upload_file"]

        system(f'rm {th_file_name}')
        
        file_name = f"media/Music/music{str(int(datetime.utcnow().timestamp()))}.mp3"

        with open(file_name,"wb+") as f:
            f.write(await music.read())

        s3 = s3Client()
        s3.upload_file(
            file_name,
            AWS_STORAGE_BUCKET_NAME,
            file_name[6:],
            ExtraArgs={"ACL": "public-read"}
        )

        system(f'rm {file_name}')
        
        music = MusicUpload()

        music.create(form["title"],AWS_BASE_URL+th_file_name[6:],form["duration"],form["category"],AWS_BASE_URL+file_name[6:])

        return JSONResponse({"message":"Uploaded","status":True})

    except Exception as e:

        return JSONResponse({"message":str(e),"status":False}, status_code=400)

async def getMusic(request):
    try:
        music = MusicUpload()

        return JSONResponse({"message":music.get(),"status":True})

    except Exception as e:
        return JSONResponse({"message":str(e),"status":False}, status_code=400)