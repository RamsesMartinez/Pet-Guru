from django.shortcuts import render

# Create your views here.
def index(request):
    template = 'index.html'    
    context={    	
    	'title': "Pet-Guru - Indice",
    }
    return render(request, template, context)

def nosotros(request):
    template = 'nosotros.html'    
    context={    	
    	'title': "Pet-Guru - Nosotros",
    }
    return render(request, template, context)

def reglamento(request):
    template = 'reglamento.html'    
    context={    	
    	'title': "Pet-Guru - Reglamento",
    }
    return render(request, template, context)



