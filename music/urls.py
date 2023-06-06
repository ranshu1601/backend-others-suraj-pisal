from starlette.routing import Route
from .views import postMusic, getMusic

music_urlpatterns=[
    Route('/music/', postMusic , methods=["POST"]),
    Route('/music/fetchmusic', getMusic , methods=["GET"]),
]
