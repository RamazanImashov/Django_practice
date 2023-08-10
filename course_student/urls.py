from django.urls import path
from .views import post_list, create_post, update_post1, delete_post, update_post2

urlpatterns = [
    path('', post_list),
    path('create/', create_post),
    path('update1/<int:id>/', update_post1),
    path('delete/<int:id>/', delete_post),
    path('update2/<int:id>/', update_post2),
]
