# Generated by Django 4.1.3 on 2023-07-29 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_product_create_at_product_discounted_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='cat_name',
        ),
        migrations.RenameField(
            model_name='main_category',
            old_name='name',
            new_name='man_name',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.category'),
        ),
    ]
