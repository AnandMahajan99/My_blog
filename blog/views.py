from django.shortcuts import render

# Create your views here.

def index(request):
    print("hhh")
    return render(request, 'blog/index.html')
