from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('remove/', views.analyze,name='punctuation'),
   # path('capital/', views.capitalizeFirst,name='letter'),
   # path('newline/', views.newlineRemove,name='remover'),
   # path('space/', views.spaceRemover,name='spacy'),
   # path('count/', views.charCount,name='charact'),
]