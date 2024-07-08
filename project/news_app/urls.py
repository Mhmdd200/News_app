from django.urls import path
from news_app.views import AuthorView, ArticleView, CommentView, CategoryView  
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('author', AuthorView, basename='author')
router.register('article', ArticleView, basename='article')
router.register('comment', CommentView, basename='comment')
router.register('category', CategoryView, basename='category')
urlpatterns = router.urls