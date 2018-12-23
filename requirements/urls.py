from django.conf.urls import url
from . import views

urlpatterns = [
    url('usecase/create/', views.usecaseCreate, name='usecase-create'),

]
