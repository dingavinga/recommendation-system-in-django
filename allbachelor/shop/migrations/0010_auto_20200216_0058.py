# Generated by Django 2.2.5 on 2020-02-15 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_remove_product_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='category/'),
        ),
        migrations.AlterModelTable(
            name='category',
            table='category',
        ),
    ]
