# Generated by Django 4.1.7 on 2023-04-17 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0008_alter_item_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_content',
            field=models.TextField(default='<h6 class="card-subtitle mb-2 text-body-secondary "> <a id="h1">Раздел 1</a></h6><p class="card-text">Содержание раздела 1</p><img src="/static/images/settings_django.png"  height="30px"><a href="#h1" class="card-link">На раздел 1</a>', verbose_name='Основное содержание'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_nav',
            field=models.CharField(default='Название ссылки', max_length=255, verbose_name='Название ссылки'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_title',
            field=models.CharField(default='Заголовок', max_length=255, verbose_name='Заголовок (title)'),
        ),
    ]