from django.contrib import admin

from .models import Animal, Kind, PostImage

admin.site.register(Animal)
admin.site.register(Kind)
admin.site.register(PostImage)


# Register your models here.
