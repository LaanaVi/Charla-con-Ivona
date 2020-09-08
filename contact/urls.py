from django.urls import path
from .views import contact, form


urlpatterns = [
    path('kontakt/', contact, name='contact'),
    path('prijava/', form, name='form')
]
