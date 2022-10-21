from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='contact'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('edit/<int:id>', views.edit, name='edit')
]
