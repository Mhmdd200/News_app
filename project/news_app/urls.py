from django.urls import path
from news_app.views import AuthorView, ArticleView
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('author', AuthorView, basename='author')
router.register('article', ArticleView, basename='article')
urlpatterns = router.urls