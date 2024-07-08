from django.db import models
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(default="this is a default value")
    email = models.EmailField(unique=True)
    profile_picture_url = models.URLField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    summary = models.CharField(max_length=500)
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=[
        ('draft','Draft'),
        ('published','Published')
    ], max_length=100)
    view_count = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    image_url = models.URLField(null=True,blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
class Comment(models.Model):
    content = models.TextField()
    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    