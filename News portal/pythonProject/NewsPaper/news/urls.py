from django.urls import path
from  .views import  AuthorList

urlpatterns = [
    path('', AuthorList.as_view())
]