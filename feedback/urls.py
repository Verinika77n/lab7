from django.urls import path
from .views import feedback_create, FeedbackList

urlpatterns = [
    path('', FeedbackList.as_view(), name='feedback-list'),
    path('add/', feedback_create, name='feedback-create'),
]
