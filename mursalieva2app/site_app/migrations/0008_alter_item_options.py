# Generated by Django 4.1.7 on 2023-04-17 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0007_alter_item_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('-item_nav_position',), 'verbose_name': 'Контент текущей страницы', 'verbose_name_plural': 'Уникальный контент страниц'},
        ),
    ]