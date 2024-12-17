from django import forms
from .models import Category, SPU

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name_zh', 'category_name_en', 'description', 
                 'image', 'parent', 'rank_id', 'level', 'is_last_level', 'status']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'parent': forms.Select(attrs={'class': 'form-select'}),
            'level': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 添加 Bootstrap 类
        for field in self.fields.values():
            if not isinstance(field.widget, (forms.CheckboxInput, forms.RadioSelect)):
                field.widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super().clean()
        parent = cleaned_data.get('parent')
        level = cleaned_data.get('level')

        if parent and level <= parent.level:
            raise forms.ValidationError('子类目的层级必须大于父类目的层级')
        elif not parent and level != 1:
            raise forms.ValidationError('没有父类目时，必须是一级分类')

        return cleaned_data 

class SPUForm(forms.ModelForm):
    class Meta:
        model = SPU
        fields = ['spu_code', 'spu_name', 'spu_remark', 'sales_channel', 
                 'category', 'status']
        widgets = {
            'spu_remark': forms.Textarea(attrs={'rows': 3}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'sales_channel': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 只显示最后一级类目
        self.fields['category'].queryset = Category.objects.filter(is_last_level=True)
        # 添加 Bootstrap 类
        for field in self.fields.values():
            if not isinstance(field.widget, (forms.CheckboxInput, forms.RadioSelect)):
                field.widget.attrs['class'] = 'form-control'
        
        # 如果是编辑模式（实例已存在），则 SPU 编码不可修改
        if self.instance and self.instance.pk:
            self.fields['spu_code'].widget.attrs.update({
                'readonly': True,
                'class': 'form-control bg-light text-muted',  # 添加置灰样式
                'tabindex': '-1'  # 禁止 Tab 键聚焦
            })
            self.fields['spu_code'].help_text = 'SPU编码不可修改'

    def clean_spu_code(self):
        code = self.cleaned_data['spu_code']
        if len(code) < 4:
            raise forms.ValidationError('SPU编码长度不能小于4个字符')
        
        # 如果是编辑模式，返回原始编码
        if self.instance and self.instance.pk:
            return self.instance.spu_code
        return code