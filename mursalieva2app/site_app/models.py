from django.db import models
from django.urls import reverse

class Item(models.Model):
    item_title = models.CharField(verbose_name = 'Заголовок (title)', max_length=255, default="Заголовок" )
    item_nav = models.CharField(verbose_name = 'Название ссылки', max_length=255, default="Название ссылки")
    item_nav_position = models.IntegerField(verbose_name = 'Приоритет в навигации (0 - исключить)', default=0,)
    item_content = models.TextField(verbose_name = 'Основное содержание',  default='<h6 class="card-subtitle mb-2 text-body-secondary "> <a id="h1">Раздел 1</a></h6><p class="card-text">Содержание раздела 1</p><img src="/static/images/settings_django.png"  height="30px"><a href="#h1" class="card-link">На раздел 1</a>')
    item_current_date = models.DateTimeField(verbose_name = "Дата Записи", auto_now=True)

    class Meta:
        verbose_name = 'Контент текущей страницы'
        verbose_name_plural = 'Уникальный контент страниц'
        ordering = ('-item_nav_position',)

    # def get_absolute_url(self):
    #     return reverse('one_page', kwargs={'id': self.pk})
    # 6.28

    def __str__(self):
        return f"id: {self.id}.  {self.item_title}"

