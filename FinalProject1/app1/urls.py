from django.urls import path
from .views import LoginPage,HomePage,LogoutPage,verify,SignupPage

app_name='hirad'

urlpatterns=[
    
    
    path('login/', LoginPage, name='login'),
    path('home/', HomePage, name='home'),
    path('logout/', LogoutPage, name='logout'),
    path('verify/<str:username>/',verify,name='verify'),
    path('signup/', SignupPage, name='signup'),
    
    
    
    ]