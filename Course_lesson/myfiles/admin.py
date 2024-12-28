from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe


from .models import *

# Register your models here.


admin.site.register(Course)


class GulAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created', 'updated', 'published', 'views', 'category', 'get_photo')
    list_display_links = ('id', 'title')
    list_editable = ('category',)
    list_filter = ('category', )
    search_fields = ('title', 'content')
    list_per_page = 10
    actions_on_top = True
    actions_on_bottom = False
    save_on_top = False
    readonly_fields = ('views',)

    def get_photo(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" width="150px">')
        return "-"

    get_photo.short_description = "Rasmi"



admin.site.register(Lesson, GulAdmin)