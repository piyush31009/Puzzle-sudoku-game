from django.urls import path
from argparse import Namespace
from . import views

urlpatterns = [
    path("",views.home, name="new_game"),
    path("check/",views.check,name="check"),
    path("get_steps/",views.get_steps, name="get_steps"),
    # path('leaderboard/',views.index,name='leaderboard'),
]
