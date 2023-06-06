from starlette.routing import Route
from .views import notification, getUserNotification

noti_urlpatterns=[
    Route('/notification/', notification , methods=["POST"]),
    Route('/notification/get', getUserNotification , methods=["GET"]),
]
