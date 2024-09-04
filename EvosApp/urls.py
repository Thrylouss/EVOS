from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='main'),
    path('manage/panel', views.Admin.as_view(), name='admin'),
    path('category', views.CategoryView.as_view(), name='categories'),
    path('category/delete/<int:cat_id>', views.delete_category, name='delete-category'),
    path('category/add', views.CategoryAdd.as_view(), name='add-category'),
    path('food', views.MealView.as_view(), name='foods'),
    path('food/add', views.MealAdd.as_view(), name='add-food'),
    path('food/delete/<int:food_id>', views.delete_food, name='delete-food'),
    path('user/orders', views.UserOrders.as_view(), name='user-orders'),
    path('order/delete/<int:order_id>', views.delete_order, name='delete-order'),
    path('product-info/', views.ProductsDetails.as_view(), name='product-info'),
    path('branches', views.BranchesView.as_view(), name='branches'),
    path('branches/<int:pk>', views.BranchInfo.as_view(), name='branch-info'),
    path('news', views.NewsView.as_view(), name='news'),
    path('about-us', views.AboutUs.as_view(), name='about-us'),
    path('contact', views.ContactView.as_view(), name='contacts'),
    path('vacancies', views.VacancyView.as_view(), name='vacancies'),
    path('vacancies/<int:pk>', views.VacancyDetail.as_view(), name='vacancy-detail'),
    path('news/<int:pk>', views.NewsDetailedView.as_view(), name='news-detailed-view'),
    path('add-employee/<int:vacancy_id>', views.AddEmployee.as_view(), name='add-employee'),
    path('submit-order/', views.SubmitOrder.as_view(), name='submit-order'),
]