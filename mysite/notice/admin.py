from django.contrib import admin

# Register your models here.
# notice/admin.py

from django.contrib import admin
from .models import Notice

class NoticeAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'writer',
        'hits',
        'registered_date',
        )
    search_fields = ('title', 'content', 'writer__user_id',)

admin.site.register(Notice, NoticeAdmin)