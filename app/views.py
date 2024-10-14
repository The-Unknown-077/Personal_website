from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile, Skill, AboutMe, Service, Portfolio, Category, Post
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404



def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    about_me = AboutMe.objects.first()
    services = Service.objects.all()
    portfolios = Portfolio.objects.all()
    categories = Category.objects.all()
    posts = Post.objects.order_by("-id")[:3]
    return render(request, "index.html", {'user': profile, 'skills':skills, 'aboutme':about_me, 'services':services, 'portfolios': portfolios, 'categories': categories, 'posts': posts})





def blog(request):
    posts = Post.objects.all()
    if request.method == 'POST' and request.POST.get('search'):
        search = request.POST.get('search')
        posts = posts.filter(title_icontains=search)

    paginator = Paginator(posts, 2)
    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)



    most_watched_posts = Post.objects.order_by('-view_count')[:3]

    return render(request, "blog.html", {'posts': posts, 'most_watched_posts': most_watched_posts})





def portfolio(request):
    
    posts = Portfolio.objects.all()
    if request.method == 'POST':
        search = (request.POST.get('search'))
        posts = posts.filter(title__icontains=search)
        
    paginator = Paginator(posts, 2)
    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)
        
    return render(request, "portfolio.html", {'posts': posts})




def about(request):
    return render(request, "about-us.html")


def portfolio(request):
    return render(request, "portfolio.html")



def blog_detail(request, pk): # pk = id
    blog = get_object_or_404(Post, id=pk)
    blog.view_count += 1
    blog.save()

    return render(request, "single-blog.html", {'blog':blog})




    













