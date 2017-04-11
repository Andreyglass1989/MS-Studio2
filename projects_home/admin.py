from django.contrib import admin
from projects_home.models import Project, Gallery, Rozdel

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    list_display = ('name','location', 'image_img', )


class ImageAdmin_item(admin.ModelAdmin):
    list_display = ( 'project_name', 'image_img', )
    list_filter = ["project", ]

admin.site.register( Project, ImageAdmin )
admin.site.register( Gallery, ImageAdmin_item)
#admin.site.register( Rozdel )
admin.site.site_header = "MS-Studio Administration"