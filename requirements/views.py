from django.shortcuts import render
from django.forms import modelform_factory
from requirements.models import Usecase

# Create your views here.
def usecaseCreate(request):
   form = modelform_factory(Usecase)
   context = {"usecaseform":form}
   return render(request,template_name="requirements/usecase-create.html",context=context)