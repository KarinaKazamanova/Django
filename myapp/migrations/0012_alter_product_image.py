# Generated by Django 4.2.6 on 2023-10-23 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='myapp/no_image.png', upload_to='myapp/'),
        ),
    ]
