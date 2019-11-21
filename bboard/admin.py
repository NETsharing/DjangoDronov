from django.contrib import admin

# Register your models here.
from .models import Bb, Moderator, TypeModeration
from .models import Rubric

class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric', 'moderator')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')
    list_filter = ('price', 'published')



admin.site.register(Rubric)
admin.site.register(Bb, BbAdmin)
admin.site.register(Moderator)
admin.site.register(TypeModeration)