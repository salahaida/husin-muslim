from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import PostEN

def all_posts_en(request):
    if 'search' in request.GET:
        search = request.GET['search']
        all_posts_en = PostEN.objects.filter(title_en=search)
    else:

        all_posts_en = PostEN.objects.all()


    context = {
    'all_posts_en' : all_posts_en,
    }

    return render(request, 'index_en.html', context)

def post_en(request, id):


    post_en = get_object_or_404(PostEN, id=id)

    context = {
    'post_en' : post_en,
    }

    return render(request, 'detal_en.html', context)

def about_en(request):
    return render(request, 'about_en.html')
def connect_en(request):
    return render(request, 'connect_en.html')
