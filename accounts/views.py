from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #register in the db
            form.save()
            return redirect('article:article_list')  # Make sure 'articles:list' is defined in your URLs
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data= request.POST)
        if form.is_valid():
            #login the user
            user = form.get_user()
            login(request,user)
            #check if user is authenticated to protected page
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('article:article_list')
    else:
        form  = AuthenticationForm()
    return render(request, 'accounts/login.html',{'form':form})

def logout_view(request):
    if request.method == 'POST':
        #user log out
        logout(request)
        return redirect('article:article_list')
