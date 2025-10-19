from django.urls import path
from .views import index, calc, feedback, ArticleDetail

urlpatterns = [
    path('', index, name='index'),
    path('calc/', calc, name='calc'),
    path('feedback/', feedback, name='feedback'),
    path('article/<slug:slug>/', ArticleDetail.as_view(), name='article-detail'),
]
