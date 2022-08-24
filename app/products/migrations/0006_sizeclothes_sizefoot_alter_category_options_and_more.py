# Generated by Django 4.0.6 on 2022-08-23 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_cat'),
    ]

    operations = [
        migrations.CreateModel(
            name='SizeClothes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Large Large'), ('XXL', 'XLarge XLarge'), ('OutOfStock', 'OutOfStock')], default='OutOfStock', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SizeFoot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.DecimalField(decimal_places=1, default=0, max_digits=3)),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.RemoveField(
            model_name='product',
            name='cat',
        ),
        migrations.AddField(
            model_name='product',
            name='cat',
            field=models.ManyToManyField(blank=True, null=True, to='products.category'),
        ),
        migrations.RemoveField(
            model_name='product',
            name='size_clothes',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size_foot',
        ),
        migrations.AddField(
            model_name='product',
            name='size_clothes',
            field=models.ManyToManyField(blank=True, null=True, to='products.sizeclothes'),
        ),
        migrations.AddField(
            model_name='product',
            name='size_foot',
            field=models.ManyToManyField(blank=True, null=True, to='products.sizefoot'),
        ),
    ]
