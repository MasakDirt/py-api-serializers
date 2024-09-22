from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionViewSet,
    GenreViewSet,
    ActorViewSet
)


app_name = "cinema"

router = routers.DefaultRouter()

router.register("cinema_halls", CinemaHallViewSet)
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)

urlpatterns = [
    path("", include(router.urls))
]
