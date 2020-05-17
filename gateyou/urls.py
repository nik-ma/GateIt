from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    

    path('content/',views.content,name='content'),
    path('signup/',views.signup,name='signup'),
    path('ecContent/',views.ecContent,name='ecContent'),
    path('studyM/',views.studyM,name='studyM'),
    path('search/',views.search,name='search'),
    path('reset/validate/',views.reset2,name='reset2'),
    path('guestContent/',views.guestContent,name='guestContent'),
    path('logout/',views.logout,name='logout'),
    path('about/',views.about,name='about'),

    
]