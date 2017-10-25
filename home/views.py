from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    template = 'index.html'    
    context={    	
    	'title': "PetGurú - Inicio",
    }
    return render(request, template, context)

def nosotros(request):
    template = 'nosotros.html'    
    context={    	
    	'title': "PetGurú - Nosotros",
    }
    return render(request, template, context)

def reglamento(request):
    template = 'reglamento.html'    
    context={    	
    	'title': "PetGurú - Reglamento",
    }
    return render(request, template, context)



