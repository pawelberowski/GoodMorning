from django.urls import path
from viewer.views import ServicesCreateView, HomeView, ServicesView, ServicesUpdateView, ServicesSelectUpdateView, \
    ProfileUpdateView, SelectProfileUpdateView, SignUpView, ChosenUpdateView, SelectChosenUpdateView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('', HomeView.as_view(), name='home'),
    path('services', ServicesView.as_view(), name='services'),
    path('add_service', ServicesCreateView.as_view()),
    path('service_update/<pk>', ServicesUpdateView.as_view(), name='service_update'),
    path('service_update', ServicesSelectUpdateView.as_view()),
    path('profile_update/<pk>', ProfileUpdateView.as_view(), name='profile_update'),
    path('profile_update', SelectProfileUpdateView.as_view(), name='profile_select'),
    path('chosen_update/<pk>', ChosenUpdateView.as_view(), name='chosen_update'),
    path('chosen_update', SelectChosenUpdateView.as_view(), name='chosen_select'),

]