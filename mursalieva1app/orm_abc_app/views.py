import datetime
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Count, Avg, Min, Max, StdDev, Sum
from .forms import CreateTaskForm
from .models import Task

def index(request):
    return render(request, 'index.html')

def datetime_nov(request):
    datetime_now = datetime.datetime.now()
    print(datetime_now)
    context = {'key': datetime_now}
    return render(request, 'datetime_now.html', context)


def var_list_dict(request):
    var_main = 2
    print(var_main)
    list_main = [1, 2, 3, 4, 5]
    print(list_main)
    dict_main = {'x': 1, 'y': 2}
    print(dict_main)
    context = {"var_main": var_main, 'list_main': list_main, 'dict_main': dict_main}
    return render(request, 'list_dict.html', context)

class TaskFormCreate(forms.Form):
    year = forms.IntegerField()

def task_form(request):
    task_form = TaskFormCreate()
    print(task_form)
    return render(request, 'task_form.html', {"task_form": task_form})


def task_get(request):
    print(request.GET)
    print(request.GET.get("year"))
    Year = request.GET.get("year")
    return HttpResponse(f"""
    <pre>
    Year = {Year}
    </pre>
    """)

def form_create_0(request):
    print('request.method: ', request.method)
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            print("\nform_is_valid:\n", form)
            form.save()
            return redirect('orm_abc_app:task_result')
    else:
        form = CreateTaskForm()
        print('\nform_else:\n', form)
    context = {'form': form}
    print("\ncontext:\n", context)
    return render(request, 'form_create_0.html', context)


def form_create(request):
    print('request.method: ', request.method)
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            print("\nform_is_valid:\n", form)
            form.save()
            return redirect('orm_abc_app:task_result')
    else:
        form = CreateTaskForm()
        print('\nform_else:\n', form)
    context = {'form': form}
    print("\ncontext:\n", context)
    return render(request, 'form_create.html', context)


def task_result(request):
    object_list = Task.objects.all().order_by('-id')[:2]
    print("object_list: ", object_list)
    # dict
    print("object_list.values('year'):", object_list.values('year',))
    last_object = object_list.values('year',)[0]
    print("last_object: ", last_object)
    print("object_0_year: ", last_object['year'])
    # list
    values_list = object_list.values_list()[0]
    print("values_list: ", values_list)

    year = values_list[2]
    leap = ((year % 4 == 0) and not (year % 100 == 0)) or (year % 400 == 0)
    century = year // 100 + 1

    # context
    task_formulation = values_list[1]
    print('task_content: ', task_formulation)
    last_data = [values_list[2]]
    print('last_data:', last_data)
    print('leap: ', leap)
    print('century: ', century)
    context = {'task_formulation': task_formulation, 'last_data': last_data, 'leap': leap, 'century': century, 'last_object': last_object}
    return render(request, 'task_result.html', context)

def table(request):
    # objects_list
    objects_values = Task.objects.values()
    print('\nobjects_values:', objects_values)
    # values_list 
    objects_values_list = Task.objects.values_list()
    print('\nobjects_values_list:', objects_values_list)
    cur_objects = Task.objects.all()
    statics_val = [cur_objects.aggregate(Count('year')), cur_objects.aggregate(Avg('year')), cur_objects.aggregate(Min('year')),
                   cur_objects.aggregate(Max('year')), cur_objects.aggregate(StdDev('year')), cur_objects.aggregate(Sum('year'))]
    print('\nstatics_val:', statics_val)
    statics = {'statics_val': statics_val}
    # fields_name
    fields = Task._meta.get_fields()
    print('\nfields', fields)
    verbose_name_list = []
    name_list = []
    for e in fields:
        verbose_name_list.append(e.verbose_name)
        name_list.append(e.name)
    print('\nverbose_name_list:', verbose_name_list)
    print('\nname_list', name_list)
    field_names = verbose_name_list
    context = {'objects_values': objects_values, 'objects_values_list': objects_values_list,  'statics': statics, 'field_names': field_names}
    return render(request, 'table.html', context)
