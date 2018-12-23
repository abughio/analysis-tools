from django.shortcuts import render

# Create your views here.

def index(request):
    context = { 'message':"hello World!! from pages index view"

    }

    return render(request,template_name="pages/home.html", context=context)
