from django.urls import path

from . import views
app_name='apps'

urlpatterns=[
    path('',views.login,name='login'),
    path("index/",views.index,name='index'),
    path('vip/',views.Vip,name='vip'),
    path('staff/',views.Staff,name='staff'),
    path('automation/',views.Automation,name='automation'),
    path('year/', views.Year, name='year'),
    path('satisfaction/', views.satisfaction, name='satisfaction'),
    path('alocater/',views.alocater,name='alocater')
]
