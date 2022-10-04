from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import *
from .models import *
from django.db.models import Q

from django.views.generic import ListView
from django.core.paginator import Paginator


def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(zapcas_list)

    return render(request, 'login.html')


def zapcas_list(request):

    user = request.user.id

    shop = Zapcas.objects.filter(user_id=user)

    context = {
        'shop': shop
    }
    return render(request, 'index.html', context)


def create_zapcas(request):
    car = Car.objects.all()
    cars_category = Cars_category.objects.all()
    ratimg = Rating.objects.all()

    form = None

    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        title = request.POST.get('title')
        priceman = request.POST.get('priceman')
        notes = request.POST.get('notes')
        carids = request.POST.get('carids')
        catid = request.POST.get('catid')
        yagday = request.POST.get('yagday')
        tel = request.POST.get('tel')

        if zip(title, priceman, notes, carids, catid, yagday, tel,):

            form = Zapcas.objects.create(title=title, priceman=priceman, carids=carids,
                                         user=user, catid=catid, yagday=yagday, notes=notes, tel=tel)
            return redirect(zapcas_list)

    car_models = Car_model.objects.all()

    context = {
        'car': car,
        'cars_category': cars_category,
        'cars': car_models,
        'ratimg':ratimg

    }
    return render(request, 'create_store.html', context)


def update(request, id):
    shop = Zapcas.objects.get(id=id)
    ratimg = Rating.objects.all()
    car = Car.objects.all()
    cars_category = Cars_category.objects.all()
    print(ratimg)


    form = None

    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        title = request.POST.get('title')
        priceman = request.POST.get('priceman')
        notes = request.POST.get('notes')
        carids = request.POST.get('carids')
        catid = request.POST.get('catid')
        yagday = request.POST.get('yagday')
        tel = request.POST.get('tel')

        if zip(title, priceman, notes, carids, catid, yagday, tel,):

            form = Zapcas.objects.update(title=title, priceman=priceman, carids=carids,
                                         user=user, catid=catid, yagday=yagday, notes=notes, tel=tel)
            return redirect(zapcas_list)

    car_models = Car_model.objects.all()

    context = {
        'car': car,
        'cars_category': cars_category,
        'cars': car_models,
        'shop': shop,
        'ratimg':ratimg


    }
    return render(request, 'update_capchas.html', context)


# class Search(ListView):

#     model = Car_model

#     template_name = 'cars.html'
#     context_object_name = 'car_model'
#     paginate_by = 6

#     def get_queryset(self):
#         return Car_model.objects.filter(name__icontains=self.request.GET.get('q'))


#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['q'] = self.request.GET.get('q')
#         return context


# def cars_search(request):

#     car = Car_model.objects.all()


#     context = {
#         'car':car,
#     }
#     return render(request, 'cars.html', context)


def update_zapcas(request, id):

    shop = Zapcas.objects.get(id=id)

    car = Car_model.objects.all()
    cars_category = Cars_category.objects.all()

    if request.method == "POST":
        form = ZapcasForm(request.POST, instance=shop)
        if form.is_valid():
            form.save()
            return redirect('zapcas_list')

    context = {
        'shop': shop,
        'form': ZapcasForm(instance=shop),
        'car': car,
        'cars_category': cars_category,
    }
    return render(request, 'update_store.html', context)


def delete_zapcas(request, id):
    shop = Zapcas.objects.get(id=id)
    shop.delete()
    return redirect(zapcas_list)


def logout(request):
    logout(request)
    return redirect('login_page')


# def delete_cars(request, id):
#     shop = Car.objects.get(id=id)
#     shop.delete()
#     return redirect(cars_list)


# def cars_list(request):
#     user = request.user.id
#     shop = Car.objects.filter(user_id=user)
#     context = {
#         'shop':shop
#     }
#     return render(request, 'cars_list.html', context)


# def update_cars(request, id):
#     car = Car.objects.get(id=id)
#     if request.method == "POST":
#         form = CarsForm(request.POST, instance=car)
#         if form.is_valid():
#             form.save()
#             return redirect('cars_list')
#     context = {
#         'car':car,
#         'form': CarsForm(instance=car),
#     }
#     return render(request, 'update_cars.html', context)


# def add_cars(request):
#     form = None
#     if request.method == 'POST':
#         user = User.objects.get(id=request.user.id)
#         id = request.POST.get('id')
#         name = request.POST.get('name')
#         if zip(id, name):
#             form = Car.objects.create(id=id, name=name, user=user)
#             return redirect(store_list)
#     return render(request, 'add_cars.html')
