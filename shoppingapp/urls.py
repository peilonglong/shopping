from django.urls import url
from shoppingapp.views import *
app_name='shopping'
urlpatterns=[
    url(r'^register$',RegisterView.as_view(),name='register'),
]