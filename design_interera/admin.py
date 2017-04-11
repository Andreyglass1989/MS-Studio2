from django.contrib import admin
from design_interera.models import Interer, Gallery_design_interera

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    list_display = ('name','location', 'image_img', )


class ImageAdmin_item(admin.ModelAdmin):
    list_display = ( 'project_name', 'image_img', )
    list_filter = ['project', ]
    #search_fields = ["name", ]

admin.site.register( Interer, ImageAdmin )
admin.site.register( Gallery_design_interera, ImageAdmin_item )
