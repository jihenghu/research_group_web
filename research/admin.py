# Register your models here.
from django.contrib import admin

from .models import Publication,Publist,Focus,Poplink,GalleryImage

admin.site.register(Publication)
admin.site.register(Publist)
admin.site.register(Focus)
# admin.site.register(Field)
admin.site.register(Poplink)
admin.site.register(GalleryImage)
