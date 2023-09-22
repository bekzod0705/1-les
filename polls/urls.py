from django.urls import path
from .views import Create,List,UpdateStatus
urlpatterns=[
    path('create/',Create.as_view()),
    path('all/',List.as_view()),
    path('update_status/<int:pk>/',UpdateStatus.as_view())
]