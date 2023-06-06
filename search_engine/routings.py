from .consumers import SearchEngineSocket
from starlette.routing import WebSocketRoute

search_socketpatterns=[
    WebSocketRoute("/ws/search", SearchEngineSocket)
]
