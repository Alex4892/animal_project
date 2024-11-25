from django.contrib import admin

from .models import Animal, Kind, PostImage, Target

admin.site.register(Animal)
admin.site.register(Kind)
admin.site.register(Target)
admin.site.register(PostImage)
