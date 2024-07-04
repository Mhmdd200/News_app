from django.shortcuts import render
from news_app.models import Article, Author, Category, Comment
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from news_app.serializer import AuthorSerializer, ArticleSerializer, getArticleSerializer
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
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data)
    def retrieve(self, request, pk=None):
        article = get_object_or_404(Article, pk=pk)
        serializer = getArticleSerializer(article)
        return Response(serializer.data)
    def create(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save
            return Response("Article created!", status=status.HTTP_201_CREATED)
        return Response('Error creating an article', status=status.HTTP_405_METHOD_NOT_ALLOWED)
    def destroy(self, request, pk=None):
        article = get_object_or_404(Article, pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)