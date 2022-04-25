from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
#class login(TemplateView):
 #   template_name = 'C:/Users/sarah/PycharmProjects/proyecto/proyecto/template/login.html'



def login(request):
    return render(request, "C:/Users/sarah/PycharmProjects/proyecto/proyecto/cfood/template/login.html")

