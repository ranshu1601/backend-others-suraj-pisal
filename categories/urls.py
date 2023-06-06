from starlette.routing import Route
from .views import videoCategories, musicCategories, getUserCategories, authenticatedCategory, subCategories

categories_urlpatterns=[
    Route('/cat/music/', musicCategories , methods=["GET","POST"]),
    Route('/cat/video/', videoCategories , methods=["GET","POST"]),
    Route('/cat/sub/', subCategories, methods=["GET", "POST"]),
    Route('/cat/user/', getUserCategories , methods=["POST"]),
    Route('/cat/auth/', authenticatedCategory , methods=["POST"]),
    
]
