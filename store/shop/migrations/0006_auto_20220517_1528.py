# Generated by Django 3.2 on 2022-05-17 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_productimages_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('text', models.TextField(max_length=5000, verbose_name='Text')),
                ('email', models.EmailField(max_length=254)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.reviews')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
            options={
                'verbose_name_plural': 'Reviews',
            },
        ),
    ]
