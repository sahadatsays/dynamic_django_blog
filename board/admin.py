from django.contrib import admin
from .models import BlogModel, NavMenu
# Register your models here.

admin.site.register(BlogModel)
@admin.register(NavMenu)
class NavMenuAdmin(admin.ModelAdmin):
    list_display = ('name','slug', 'prent_menu', 'parent')
