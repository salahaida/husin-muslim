from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Posts

def all_posts(request):
    if 'search' in request.GET:
        search = request.GET['search']
        all_posts = Posts.objects.filter(title=search)
    else:

        all_posts = Posts.objects.all()


    context = {
    'all_posts' : all_posts,
    }

    return render(request, 'index.html', context)

def post(request, id):


    post = get_object_or_404(Posts, id=id)

    context = {
    'post' : post,
    }

    return render(request, 'detal.html', context)


def about(request):
    return render(request, 'about.html')
def connect(request):
    return render(request, 'connect.html')
