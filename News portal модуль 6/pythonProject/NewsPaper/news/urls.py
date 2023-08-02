from django.urls import path
from .views import PostsList, PostsDetal

urlpatterns = [
    path('', PostsList.as_view()),
    path('<int:pk>', PostsDetal.as_view())
]