from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.index, name='index'),
    path('note/add/', views.add_note, name='add_note'),
    path('note/<int:pk>/', views.note_detail, name='note_detail'),
    path('note/<int:pk>/delete/', views.delete_note, name='delete_note'),
    path('about/', views.about, name='about'),
]

