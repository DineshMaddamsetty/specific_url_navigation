from django.urls import path
from sivani.views import *
app_name='nothing'
urlpatterns=[
    path('siva/',siva,name='siva'),
    
]