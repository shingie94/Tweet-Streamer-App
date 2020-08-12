from django.urls import path
from app import views

urlpatterns = [
    path('',views.MyView.as_view(),name='my_view'),
    # path('',views.tweet_search,name='tweet_search'),
]
