from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Car, Comment, Profile
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404


def index(request):
    cars = Car.objects.all()
    return render(request, 'index.html', {'cars': cars})


def detail(request, car_id):
    try:
        c = Car.objects.get(id=car_id)
    except:
        raise Http404("Автомобиль не найден!!!")

    lates_comments_list = c.comment_set.order_by('-id')[:10]

    return render(request, 'detail.html', {'car': c, 'lates_comments_list': lates_comments_list})


def add_comment(request, car_id):
    try:
        c = Car.objects.get(id=car_id)
    except:
        raise Http404("Автомобиль не найден!!!")
    c.comment_set.create(comment_author_name=request.POST['name'], comment_text=request.POST['text'])
    return HttpResponseRedirect(reverse('detail', args=(c.id,)))


def delete_car(request, car_id):
    c = Car.objects.get(id=car_id)
    c.delete()
    return HttpResponseRedirect(reverse('index'))


def personalCabinet(request):
    cars = Car.objects.all()
    return render(request, 'personalCabinet.html', {'cars': cars})


class ProfileDetail(DetailView):
    model = Profile
    template_name = "user_profile.html"
