from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):

    template = 'index.html'    
    context={    	
    	'title': "Pet-Guru - Indice",
    }
    return render(request, template, context)

def nosotros(request):

    if request.method == 'POST':        
        print("entra")
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, email=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            print("Valido")
            return redirect('home:reglamento')
            ...
        else:
            # Return an 'invalid login' error message.
            print("No valido")
            return redirect('home:index')
            
            ...
            

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



