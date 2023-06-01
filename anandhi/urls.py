from django.urls import path
from anandhi.views import *
app_name='something'
urlpatterns=[
    path('anandh/',anandh,name='anandh'),

]