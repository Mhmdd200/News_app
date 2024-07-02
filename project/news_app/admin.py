from django.contrib import admin
from news_app import models
admin.site.register(models.Article)
admin.site.register(models.Author)
admin.site.register(models.Category)
admin.site.register(models.Comment)
# Register your models here.
