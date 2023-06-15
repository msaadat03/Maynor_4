# import datetime
from django.db import models

class Task(models.Model): 
    task = models.CharField(verbose_name="Формулировка  задачи", default="Известен год. Определить, будет ли этот год високосным, и к какому веку этот год относится.", max_length=255)
    year = models.IntegerField()
    current_date = models.DateTimeField(verbose_name="Дата изменения(save)", auto_now=True)

    def __str__(self):
        # return self.task
        # return '%s %s' % (self.task, self.current_date)
        return f"{self.id}&{self.task}"


    class Meta:
        verbose_name = "Year"
        verbose_name_plural = "Years"
        ordering = ('-id', '-year')




# current_date = models.DateTimeField("ДатаВремя", default=datetime.datetime.now())
# current_date = models.DateTimeField("ДатаВремя", auto_now_add=True)


# python manage.py makemigrations
# python manage.py migrate


# admin.py
# from django.contrib import admin
# # Register your models here.
# from .models import Abc
# admin.site.register(Abc)


# forms.py
# from django.forms import ModelForm
# from .models import Abc
#
# class CreateAbcForm(ModelForm):
#     class Meta:
#         model = Abc
#         fields = ['task', 'a' ,'b' ,'c', 'c_calc']
