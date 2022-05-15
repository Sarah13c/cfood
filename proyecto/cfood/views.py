from django.shortcuts import render
from django.template import loader
from django.http import Http404
from django.views.generic import TemplateView
from django.shortcuts import      HttpResponse
from .models import Recipes

def detail(request, recipes_id):
    try:
        recipe = Recipes.objects.get(pk=recipes_id)
    except Recipes.DoesNotExist:
        raise Http404("la receta no existe")
    #return HttpResponse(" Esta es la receta %s" % recipes_id)
    return render(request, 'cfood/detail.html', {'Recipes': Recipes})

def index(request):
    template =loader.get_template('cfood/login.html')
    latest_recipes_list = Recipes.objects.order_by('recipes_id')[:5]
    output = ''.join([q.description for q in latest_recipes_list])
    context = {'latest_recipes_list': latest_recipes_list}
    return render(request, 'cfood/login.html', context)

# Create your views here.
#class login(TemplateView):
 #   template_name = 'C:/Users/sarah/PycharmProjects/proyecto/proyecto/template/login.html'



def login(request):
    return render(request, "C:/Users/sarah/PycharmProjects/proyecto/proyecto/cfood/template/login.html")

