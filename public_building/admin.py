from django.contrib import admin
from public_building.models import Building, Gallery_building

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    list_display = ('name','location', 'image_img', )


class ImageAdmin_item(admin.ModelAdmin):
    list_display = ( 'project_name', 'image_img', )
    list_filter = ["project", ]

admin.site.register( Building, ImageAdmin )
admin.site.register( Gallery_building, ImageAdmin_item)
