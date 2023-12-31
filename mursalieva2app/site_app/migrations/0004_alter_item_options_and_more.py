# Generated by Django 4.1.7 on 2023-03-30 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0003_alter_item_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('-item_nav_position',), 'verbose_name': 'Содержание фрагмента', 'verbose_name_plural': 'Содержание фрагментов'},
        ),
        migrations.RenameField(
            model_name='item',
            old_name='current_date',
            new_name='item_current_date',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='nav_position',
            new_name='item_nav_position',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='title_item',
            new_name='item_title',
        ),
        migrations.RemoveField(
            model_name='item',
            name='content',
        ),
        migrations.RemoveField(
            model_name='item',
            name='nav_item',
        ),
        migrations.AddField(
            model_name='item',
            name='item_content',
            field=models.TextField(default='', verbose_name='Основное содержание фрагмента'),
        ),
        migrations.AddField(
            model_name='item',
            name='item_nav',
            field=models.CharField(default='Фрагмент в навигации', max_length=255, verbose_name='Фрагмент в навигации (0 - исключить)'),
        ),
    ]
