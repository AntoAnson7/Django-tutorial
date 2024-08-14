from django.contrib import admin
from django.urls import path
from .views import test, home, user_page, index, formdata, register_student, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', test, name='test'),
    path('home/', home, name='home'),
    path('index/', index, name='index'),
    path('reg/', formdata, name='formdata'),
    path('register/', register_student, name='register'),
    path('login/', login_view, name='login'),  
    path('logout/', logout_view, name='logout'),  
    path('user/', user_page, name='user_page'),  
    # path('success/', registration_success, name='registration_success'),
]
