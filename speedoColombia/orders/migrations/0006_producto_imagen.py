# Generated by Django 4.2.1 on 2023-06-15 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_producto_descripcion_corta_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='imagesPropducts/'),
        ),
    ]