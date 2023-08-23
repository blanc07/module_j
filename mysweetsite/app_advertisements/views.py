from django.shortcuts import render, redirect   # переадресация
from .models import Advertisement
from .forms import AdvertisementModelForm
from django.urls import reverse     # метод для получения ссылки по названию в параметре name
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse

# Create your views here.


def index(request):
    advertisements = Advertisement.objects.all()
    context = {
        'advertisements': advertisements
    }
    return render(request, 'index.html', context)


def top_sellers(request):
    return render(request, 'top-sellers.html')


# проверка POST или GET запрос


def post_adv(request: WSGIRequest):
    # print(type(request))
    if request.method == 'POST':
        form = AdvertisementModelForm(request.POST, request.FILES)    # передаем данные и медиа в экземпляр формы
        if form.is_valid():     # проверяем правильость заполнения формы
            adv = Advertisement(**form.cleaned_data)    # передаю данные пользователя в БД
            adv.user = request.user     # узнаю пользователя по запросу и передаю в БД
            adv.save()  # сохраняем запись
            return redirect(    # переадресация на главную страницу
                reverse('start')
            )
    else:
        # GET запрос
        form = AdvertisementModelForm()  # экземпляр формы

    context = {'forms': form}
    return render(request, 'advertisement-post.html', context)
