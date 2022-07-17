from django.contrib import admin
from .models import Link
# Register your models here.

class LinkDB(admin.ModelAdmin):
    list_display = [
        'target_url','author','description','identifier','created_date','active'
    ]


admin.site.register(Link, LinkDB)