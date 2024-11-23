from django.urls import path

from .views import (view_detail_group)

app_name = "groups"

urlpatterns = [
        path('detail_groups/', view_detail_group,
             name='detail_groups'),
]
