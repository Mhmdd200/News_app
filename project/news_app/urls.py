from django.urls import path
from news_app.views import AuthorView
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('author', AuthorView, basename='author')
urlpatterns = router.urls