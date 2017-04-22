from django.contrib import admin
from partner.models import Gallery

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    list_display = ( 'link', 'image_img',)


admin.site.register( Gallery, ImageAdmin)
