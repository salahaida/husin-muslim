from django.contrib import admin
from .models import PostEN

# Register your models here.
class PostENAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content']
admin.site.register(PostEN, PostENAdmin)
