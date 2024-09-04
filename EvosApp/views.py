import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView, ListView, DeleteView, CreateView, DetailView
from .models import Basket, Order, OrderItem, Category, Meal, Requirements, Vacancy, News, About, Branches, Employee
from .forms import CategoryForm, MealForm, EmployeeForm


# Create your views here.
@method_decorator(login_required(login_url='signIn'), name='dispatch')
class Index(ListView):
    model = Category
    template_name = 'EvosApp/user/main.html'
    context_object_name = 'categories'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['newses'] = News.objects.all()
        context['baskets'] = Basket.objects.all()
        return context


class AddEmployee(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'EvosApp/user/add_employee.html'
    success_url = reverse_lazy('main')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        vacancy_id = self.kwargs.get('vacancy_id')
        vacancy = get_object_or_404(Vacancy, id=vacancy_id)
        kwargs['user'] = self.request.user
        kwargs['vacancy'] = vacancy
        return kwargs


class SubmitOrder(View):
    def post(self, request, *args, **kwargs):
        user = request.user
        data = json.loads(request.body)
        basket_data = data.get('data')

        if not basket_data:
            return JsonResponse({'success': False, 'message': 'No data received'})

        order = Order.objects.create(user_id=user)

        for item in basket_data:
            meal_id = item.get('id')
            quantity = item.get('quantity', 1)

            try:
                meal = Meal.objects.get(id=meal_id)
                OrderItem.objects.create(order=order, meal=meal, quantity=quantity)
            except Meal.DoesNotExist:
                return JsonResponse({'success': False, 'message': f'Meal with ID {meal_id} not found'})

        return JsonResponse({'success': True})


class ProductsDetails(ListView):
    model = Meal
    template_name = 'EvosApp/user/product_composition.html'
    context_object_name = 'meals'


class BranchesView(ListView):
    model = Branches
    template_name = 'EvosApp/user/branches.html'
    context_object_name = 'branches'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['branches'] = Branches.objects.all().values('name', 'address', 'latitude', 'longitude')
        context['branches'] = json.dumps(list(context['branches']))
        context['branchess'] = Branches.objects.all()
        return context


class BranchInfo(DetailView):
    model = Branches
    template_name = 'EvosApp/user/branch-info.html'
    context_object_name = 'branch'


class AboutUs(ListView):
    model = About
    template_name = 'EvosApp/user/about-us.html'
    context_object_name = 'abouts'


class ContactView(ListView):
    model = Branches
    template_name = 'EvosApp/user/contacts.html'
    context_object_name = 'branches'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['branches'] = Branches.objects.all().values('name', 'address', 'latitude', 'longitude')
        context['branches'] = json.dumps(list(context['branches']))
        return context


class VacancyView(ListView):
    model = Vacancy
    template_name = 'EvosApp/user/vacancies.html'
    context_object_name = 'vacancies'


class VacancyDetail(DetailView):
    model = Vacancy
    template_name = 'EvosApp/user/vacancy-detail.html'
    context_object_name = 'vacancy'


class NewsDetailedView(DetailView):
    model = News
    template_name = 'EvosApp/user/news_detailed_view.html'
    context_object_name = 'newses'


class NewsView(ListView):
    model = News
    template_name = 'EvosApp/user/news.html'
    context_object_name = 'newses'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['newses'] = News.objects.all()[0]
        context['newsesMini'] = News.objects.all().reverse()[1:]
        return context


class Admin(TemplateView):
    template_name = 'EvosApp/admin/admin.html'


class CategoryView(ListView):
    model = Category
    template_name = 'EvosApp/admin/admin_category.html'
    context_object_name = 'categories'


class CategoryAdd(CreateView):
    form = CategoryForm
    model = Category
    template_name = 'EvosApp/admin/admin_add_category.html'
    fields = ['name']
    success_url = reverse_lazy('categories')


def delete_category(request, cat_id):
    category = Category.objects.get(id=cat_id)
    category.delete()
    return redirect('categories')


def delete_food(request, food_id):
    food = Meal.objects.get(id=food_id)
    food.delete()
    return redirect('foods')


def delete_order(request, order_id):
    order = Order.objects.get(id=order_id)
    order.delete()
    return redirect('user-orders')


class MealView(ListView):
    model = Meal
    template_name = 'EvosApp/admin/admin_meal.html'
    context_object_name = 'foods'


class MealAdd(CreateView):
    form = MealForm
    model = Meal
    fields = ['name', 'category', 'price', 'image']
    template_name = 'EvosApp/admin/admin-add-meal.html'
    success_url = reverse_lazy('foods')


class UserOrders(ListView):
    model = OrderItem
    template_name = 'EvosApp/admin/admin_user_orders.html'
    context_object_name = 'orders'
