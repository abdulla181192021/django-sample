
from django.contrib import admin
from django.urls import path
from django.urls import include
from auth_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('auth_app.urls'))
]
