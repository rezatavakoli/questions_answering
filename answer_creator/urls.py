from django.conf.urls import url
from .views import get_answers

urlpatterns = [
    url(r'^get-answers/$', get_answers)
]