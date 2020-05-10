from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('content/',views.content,name='content'),
    path('signup/',views.signup,name='signup'),
    path('something/',views.something,name='something'),
    path('studyM/',views.studyM,name='studyM'),
    
    
]