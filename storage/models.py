from django.db import models

class Stock(models.Model):
    stock_num = models.IntegerField(verbose_name='库存数量', default=0)
    warehouse = models.CharField(verbose_name='仓库', max_length=10)
    avg_cost = models.DecimalField(verbose_name='平均成本', max_digits=10, decimal_places=2, default=0)
    sku = models.ForeignKey('SKU', verbose_name='SKU', on_delete=models.CASCADE, related_name='stocks')
    created_at = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    class Meta:
        verbose_name = '库存'
        verbose_name_plural = verbose_name
        db_table = 'stock'

    def __str__(self):
        return f'{self.warehouse}-{self.sku.name}-{self.stock_num}'
