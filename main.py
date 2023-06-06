from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
import uvicorn
from server.urls import urlpatterns

middleware=[
        Middleware(CORSMiddleware,allow_origins=["*"],allow_headers=["*"],allow_methods=["*"],)
]

app = Starlette(routes=urlpatterns, middleware=middleware)

#app = Starlette(routes=urlpatterns)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", debug=False, reload=True)
