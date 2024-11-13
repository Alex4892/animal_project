from django.contrib import admin

from .models import Animal, House, Kind

admin.site.register(Animal)
admin.site.register(House)
admin.site.register(Kind)

# Register your models here.
