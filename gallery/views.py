from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Category

# Create your views here.

class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'gallery/category_list.html'
    context_object_name = 'categories'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Category.objects.all()
        # 添加搜索功能
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(
                category_name_zh__icontains=search_query
            ) | queryset.filter(
                category_name_en__icontains=search_query
            )
        return queryset.order_by('rank_id', 'id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        return context
