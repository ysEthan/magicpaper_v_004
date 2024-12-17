from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
] 