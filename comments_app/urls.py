from django.urls import path
from .views import add_comment_view, edit_comment_view, delete_comment_view


app_name = "comments"

urlpatterns = [
    path('add_comment/<int:animal_id>', add_comment_view, name='add_comment'),
    path('edit_comment/<int:comment_id>/<int:animal_id>/', edit_comment_view, name='edit_comment'),
    path('delete/<int:comment_id>/<int:animal_id>/', delete_comment_view, name='delete_comment'),
]
