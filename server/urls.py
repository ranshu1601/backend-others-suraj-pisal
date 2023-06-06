from starlette.routing import Route
from .views import page_not_found
from music.urls import music_urlpatterns
from categories.urls import categories_urlpatterns
from help.urls import help_urlpatterns
from explore.urls import explore_urlpatterns
from search_engine.routings import search_socketpatterns
from notification.urls import noti_urlpatterns

urlpatterns=[
    Route('/', page_not_found, methods=["GET","POST"]),
]

urlpatterns.extend(music_urlpatterns)
urlpatterns.extend(categories_urlpatterns)
urlpatterns.extend(explore_urlpatterns)
urlpatterns.extend(search_socketpatterns)
urlpatterns.extend(noti_urlpatterns)
urlpatterns.extend(help_urlpatterns)
