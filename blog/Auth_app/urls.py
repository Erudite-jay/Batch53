from . import views
from django.urls import path

urlpatterns=[
    path('ph/',views.print_hello),
    path('home/',views.home_page),
    path('all-data/',views.all_data),
    path('sud/<int:pk>',views.single_user_data)
]