from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('services/<int:service_id>/', views.service_detail, name='service_detail'),
    path('specialists/', views.specialists, name='specialists'),
    path('specialists/<int:specialist_id>/', views.specialist_detail, name='specialist_detail'),
    path('reviews/', views.reviews, name='reviews'),
    path('faq/', views.faq, name='faq'),
    path('contacts/', views.contact, name='contacts'),
    path('vacancies/', views.vacancies, name='vacancies'),
    path('tips/', views.tips, name='tips'),
    path('login/', views.login, name='login'),
    path('appointment/', views.appointment, name='appointment'),
    path('clinic/', views.clinic, name='clinic'),
    path('dentistry/', views.dentistry, name='dentistry'),
    path('search/', views.search, name='search'),
]