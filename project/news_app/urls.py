from django.urls import path, include
from news_app.views import AuthorView, ArticleView, CommentView, CategoryView  
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('author', AuthorView, basename='author')
router.register('comment', CommentView, basename='comment')
router.register('category', CategoryView, basename='category')
urlpatterns = [
    path('', include(router.urls)),  
    path('articles/', ArticleView.as_view({'get': 'list', 'post': 'create'}), name='article-list-create'),
    path('articles/<int:pk>/', ArticleView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='article-detail'),
]
