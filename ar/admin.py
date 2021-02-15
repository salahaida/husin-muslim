from django.contrib import admin
from .models import Posts

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content']
admin.site.register(Posts, PostAdmin)
