# Generated by Django 4.2.16 on 2024-12-18 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sku',
            name='other_dimensions',
        ),
        migrations.RemoveField(
            model_name='sku',
            name='unit_price',
        ),
        migrations.AlterField(
            model_name='sku',
            name='color',
            field=models.CharField(max_length=32, verbose_name='颜色'),
        ),
        migrations.AlterField(
            model_name='sku',
            name='height',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='高度(mm)'),
        ),
        migrations.AlterField(
            model_name='sku',
            name='img_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='图片URL'),
        ),
        migrations.AlterField(
            model_name='sku',
            name='length',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='长度(mm)'),
        ),
        migrations.AlterField(
            model_name='sku',
            name='material',
            field=models.CharField(default='无', max_length=100, verbose_name='材质'),
        ),
        migrations.AlterField(
            model_name='sku',
            name='plating_process',
            field=models.CharField(choices=[('none', '无电镀'), ('gold', '镀金'), ('silver', '镀银'), ('nickel', '镀镍'), ('chrome', '镀铬'), ('copper', '镀铜'), ('other', '其他')], max_length=32, verbose_name='电镀工艺'),
        ),
        migrations.AlterField(
            model_name='sku',
            name='provider_name',
            field=models.CharField(max_length=128, verbose_name='供应商名称'),
        ),
        migrations.AlterField(
            model_name='sku',
            name='sku_code',
            field=models.CharField(max_length=32, unique=True, verbose_name='SKU编码'),
        ),
        migrations.AlterField(
            model_name='sku',
            name='sku_name',
            field=models.CharField(max_length=128, verbose_name='SKU名称'),
        ),
        migrations.AlterField(
            model_name='sku',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='重量(g)'),
        ),
        migrations.AlterField(
            model_name='sku',
            name='width',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='宽度(mm)'),
        ),
    ]