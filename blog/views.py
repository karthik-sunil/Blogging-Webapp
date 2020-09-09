from django.shortcuts import render
from .models import Post
#from django.http import HttpResponse
#home view
def home(request):
    context = {
        'posts':Post.objects.all()    }
    return render(request,'blog/home.html', context)
#about view
def about(request):
    return render(request,'blog/about.html', {'title':'About'})

# Create your views here.
