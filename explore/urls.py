from starlette.routing import Route
from .views import explore, exploreVideo,exploreLiveSpaceCategory, trendingLiveSpace,categoryVideoOld,UserTopProfile,topProfiles,publicEvents,rooms,liveRooms, roomRecordings

explore_urlpatterns=[
    Route('/explore', explore , methods=["GET"]),
    Route('/unauth/explore/{device_id:str}', explore , methods=["GET"]), 
    Route('/trending/rooms/{page:int}', trendingLiveSpace, methods=["GET"]),
    Route('/suggested/video/{user_id:str}/{page:int}', exploreVideo , methods=["GET"]), 
    Route('/suggested/liverooms/{user_id:str}/{page:int}', exploreLiveSpaceCategory , methods=["GET"]),
    Route('/publicEvents', publicEvents , methods=["GET"]),
    Route('/rooms/{page:int}', rooms , methods=["GET"]),
    Route('/liverooms', liveRooms , methods=["GET"]),
    Route('/topProfiles/{page:int}', topProfiles , methods=["GET"]),
    Route('/UserTopProfile/{user_id:str}/{page:int}', UserTopProfile , methods=["GET"]), 
    Route('/categoryVideoOld', categoryVideoOld , methods=["GET"]),
    Route('/roomRecordings/{page:int}', roomRecordings , methods=["GET"]),
]
