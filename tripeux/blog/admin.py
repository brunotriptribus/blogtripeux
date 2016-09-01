from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'author', 'created_date', 'published_date')
    search_fields = ('title', 'author')
    list_filter = ('published_date',)
    date_hierarchy = 'published_date'
    ordering = ('-published_date',)

admin.site.register(Post, PostAdmin)

# Register your models here.
