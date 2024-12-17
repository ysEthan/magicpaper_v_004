from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('categories/add/', views.CategoryCreateView.as_view(), name='category_add'),
    path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),
    path('spus/', views.SPUListView.as_view(), name='spu_list'),
    path('spus/add/', views.SPUCreateView.as_view(), name='spu_add'),
    path('spus/<int:pk>/', views.SPUUpdateView.as_view(), name='spu_edit'),
    path('spus/<int:pk>/delete/', views.SPUDeleteView.as_view(), name='spu_delete'),
] 