from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from .models import Category, SPU
from .forms import CategoryForm, SPUForm

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

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'gallery/category_form.html'
    success_url = reverse_lazy('gallery:category_list')

    def form_valid(self, form):
        messages.success(self.request, '类目创建成功！')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '类目创建失败，请检查输入！')
        return super().form_invalid(form)

class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('gallery:category_list')
    template_name = 'gallery/category_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        try:
            result = super().delete(request, *args, **kwargs)
            messages.success(request, '类目删除成功！')
            return result
        except Exception as e:
            messages.error(request, f'删除失败：{str(e)}')
            return redirect('gallery:category_list')

class SPUListView(LoginRequiredMixin, ListView):
    model = SPU
    template_name = 'gallery/spu_list.html'
    context_object_name = 'spus'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = SPU.objects.select_related('category').all()
        # 添加搜索功能
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(
                spu_name__icontains=search_query
            ) | queryset.filter(
                spu_code__icontains=search_query
            )
        return queryset.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        return context

class SPUCreateView(LoginRequiredMixin, CreateView):
    model = SPU
    form_class = SPUForm
    template_name = 'gallery/spu_form.html'
    success_url = reverse_lazy('gallery:spu_list')

    def form_valid(self, form):
        messages.success(self.request, 'SPU创建成功！')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'SPU创建失败，请检查输入！')
        return super().form_invalid(form)

class SPUDeleteView(LoginRequiredMixin, DeleteView):
    model = SPU
    success_url = reverse_lazy('gallery:spu_list')
    template_name = 'gallery/spu_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        try:
            result = super().delete(request, *args, **kwargs)
            messages.success(request, 'SPU删除成功！')
            return result
        except Exception as e:
            messages.error(request, f'删除失败：{str(e)}')
            return redirect('gallery:spu_list')

class SPUUpdateView(LoginRequiredMixin, UpdateView):
    model = SPU
    form_class = SPUForm
    template_name = 'gallery/spu_form.html'
    success_url = reverse_lazy('gallery:spu_list')

    def form_valid(self, form):
        messages.success(self.request, 'SPU更新成功！')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'SPU更新失败，请检查输入！')
        return super().form_invalid(form)
