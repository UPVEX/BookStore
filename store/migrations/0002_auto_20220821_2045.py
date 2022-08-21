# Generated by Django 3.2 on 2022-08-21 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Book', 'verbose_name_plural': 'Books'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categorys'},
        ),
        migrations.AlterModelOptions(
            name='writer',
            options={'verbose_name': 'Writer', 'verbose_name_plural': 'Writers'},
        ),
        migrations.AlterModelTable(
            name='book',
            table='Book',
        ),
        migrations.AlterModelTable(
            name='category',
            table='Category',
        ),
        migrations.AlterModelTable(
            name='writer',
            table='Writer',
        ),
    ]