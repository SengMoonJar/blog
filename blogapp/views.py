from django.shortcuts import render,get_object_or_404,redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import CreateArticle

# Create your views here.
def home_view(request):
    return render(request,'blogapp/home.html')

def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request,'articles/article_list.html',{'articles':articles})

def article_detail(request,slug):
    article = get_object_or_404(Article,slug= slug)
    return render(request,'articles/article_detail.html',{'article':article})

@login_required(login_url='/accounts/login/')
def create_article(request):
    form = CreateArticle(request.POST,request.FILES)
    if form.is_valid():
        #save db
        instance= form.save(commit=False)
        instance.author = request.user
        form.save()
        return redirect('article:article_list')
    return render(request,'articles/create_article.html',{'form':form})