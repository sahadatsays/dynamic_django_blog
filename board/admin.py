from django.contrib import admin
from .models import BlogModel, NavMenu, PrimaryNav, SubNav
# Register your models here.

admin.site.register(BlogModel)


class SubNavInline(admin.TabularInline):
     model = SubNav 
     extra = 3
     fieldsets = (
          (
               None, {
                    'fields': ('name', 'slug')
               }
          ),
     )

class PrimaryNavAdmin(admin.ModelAdmin):
     list_display = ('name', 'parent', 'slug', 'primary')
     list_editable = ('parent', )
     fieldsets = (
          (
               None, {
                    'fields': ('name', 'slug', 'primary')
               }
          ),
     )
     inlines = (SubNavInline,)
admin.site.register(PrimaryNav, PrimaryNavAdmin)

@admin.register(NavMenu)
class NavMenuAdmin(admin.ModelAdmin):
    list_display = ('name','slug', 'prent_menu', 'parent')
