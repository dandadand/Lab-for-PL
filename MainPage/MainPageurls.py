from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.news_view),

]