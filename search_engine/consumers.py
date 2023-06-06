from starlette.endpoints import WebSocketEndpoint
from .models import SearchEngine
from json import dump

class SearchEngineSocket(WebSocketEndpoint):
    encoding = 'json'

    async def on_connect(self, websocket):
        
        await websocket.accept()
        self.search = SearchEngine()

    async def on_receive(self, websocket, data):

        if data["type"]=="creator":
            await websocket.send_json(self.search.searchPublicProfile(data["keyword"]))
        
        if data["type"]=="video":
            await websocket.send_json(self.search.searchVideo(data["keyword"]))

        if data["type"]=="myspace":
            await websocket.send_json(self.search.searchMyspace(data["keyword"]))


    async def on_disconnect(self, websocket, close_code):

        await websocket.close()
        self.search.close()