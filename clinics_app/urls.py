from django.urls import path

from .views import (view_detail_clinic)

app_name = "clinics"

urlpatterns = [
        path('detail_clinics/', view_detail_clinic, name='detail_clinics'),

]
