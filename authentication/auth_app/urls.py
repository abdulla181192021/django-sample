from django.urls import path
from auth_app import views
#for taking pictures as url in database
from django.conf import settings
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns
app_name='login_app'
urlpatterns=[
path('',views.index,name='index'),
path('register/',views.register,name='register'),
path('login/',views.login_page,name='login_page'),
path('user_login',views.user_login,name='user_login'),
path('user_logout',views.user_logout,name='user_logout')
]
urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
