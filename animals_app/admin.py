from django.contrib import admin

from .models import Animal, Kind, PostImage, Target, House

admin.site.register(Animal)
admin.site.register(Kind)
admin.site.register(Target)
admin.site.register(House)
admin.site.register(PostImage)


# Register your models here.
