from django.shortcuts import render
from news_app.models import Article, Author, Category, Comment
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from news_app.serializer import AuthorSerializer, ArticleSerializer, getArticleSerializer, CommentSerializer, CategorySerializer
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
class AuthorView(viewsets.ViewSet):
    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAuthenticated()]
    def list(self, request):
        author = Author.objects.all()
        serializer = AuthorSerializer(author,many=True)
        return Response(serializer.data)
    def retrieve(self, request, pk=None):
        author = get_object_or_404(Author, pk=pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)
    def create(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("Error creating author!", status=status.HTTP_405_METHOD_NOT_ALLOWED)
    def destroy(self, request, pk=None):
        author = get_object_or_404(Author, pk=pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class ArticleView(viewsets.ViewSet):
    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAuthenticated()]
    def list(self, request):
        article = Article.objects.all()
        serializer = getArticleSerializer(article, many=True)
        return Response(serializer.data)
    def retrieve(self, request, pk=None):
        article = get_object_or_404(Article, pk=pk)
        serializer = getArticleSerializer(article)
        return Response(serializer.data)
    def create(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Article created!", status=status.HTTP_201_CREATED)
        return Response('Error creating an article', status=status.HTTP_405_METHOD_NOT_ALLOWED)
    def destroy(self, request, pk=None):
        article = get_object_or_404(Article, pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class CategoryView(viewsets.ViewSet):
    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAuthenticated()]
    def list(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)
    def retrieve(self, request, pk=None):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    def create(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Category created!', status=status.HTTP_201_CREATED)
        return Response("Couldn't create category", status=status.HTTP_403_FORBIDDEN)
    def destroy(self, request, pk=None):
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return Response("Successfully deleted!")
class CommentView(viewsets.ViewSet):
    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAuthenticated()]
    def list(self, request):
        comment = Comment.objects.all()
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)
    def retrieve(self, request, pk=None):
        comment = get_object_or_404(Comment, pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    def create(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Comment created", status=status.HTTP_201_CREATED)
        return Response("Error couldn't create a comment", 
                        status=status.HTTP_403_FORBIDDEN)
    def destroy(self, request, pk=None):
        comment = get_object_or_404(Comment, pk=pk)
        comment.delete()
        return Response("Successfully deleted!")
    