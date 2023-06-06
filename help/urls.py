from starlette.routing import Route
from .views import sendMessage, getMessage

help_urlpatterns=[
    Route('/message', sendMessage, methods=["POST"]),
    Route('/get/message', getMessage, methods=["GET"]), 
]