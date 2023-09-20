from django.urls import path
from .views import CreateApiView,ListApiView,UpdateStatus
urlpatterns=[
    path('create/',CreateApiView.as_view()),
    path('all/',ListApiView.as_view()),
    path('update_status/<int:news_id>/',UpdateStatus.as_view)
]