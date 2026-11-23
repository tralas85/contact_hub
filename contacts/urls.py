from django.urls import path
from .views import index, search_contacts, create_contact,delete_contact

urlpatterns = [
    path('', index, name='index'),
    path('search/', search_contacts, name='search'),
    path('create/', create_contact, name='create-contact'),
    path('delete/<int:pk>/', delete_contact, name='delete-contact' ),
]