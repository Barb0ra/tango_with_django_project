from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    #construct a dictionary to pass to the template engine as its context.
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)
    
def about(request):
    return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")