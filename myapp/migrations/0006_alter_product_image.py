# Generated by Django 4.2.6 on 2023-10-21 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='/media/no_image.png', upload_to='products/'),
        ),
    ]
