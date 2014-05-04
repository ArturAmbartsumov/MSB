from django.contrib import admin
from main.models import *

# Register your models here.
admin.site.register(Articles)
admin.site.register(ArticleDescriptions)
admin.site.register(Departments)
admin.site.register(Projects)
admin.site.register(News)