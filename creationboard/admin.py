from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Article)
admin.site.register(models.Video)
admin.site.register(models.Category)
admin.site.register(models.AboutUs)
admin.site.register(models.Team)