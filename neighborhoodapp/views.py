from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from neighborhoodapp.models import Business, Post, Profile, Neighbourhood
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from neighborhoodapp.forms import SignUpForm, UpdateProfileForm, UpdateUserForm, NewNeighbourhoodForm
from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.
def index(request):
    neighbourhoods = Neighbourhood.objects.all()
    return render(request, 'index.html', {"neighbourhoods": neighbourhoods})

@login_required(login_url='/accounts/login/')
def view_neighbourhood(request, id):
    neighbourhood = Neighbourhood.objects.get(id=id)
    business = Business.objects.filter(business_neighbourhood=id)
    post = Post.objects.filter(neighbourhood=id)

    # current_user = request.user
    return render(request, 'view-neighbourhood.html',  {
        'neighbourhood': neighbourhood,'business':business,'post': post
    })

@login_required(login_url='/accounts/login/')
def search(request):
    if 'business' in request.GET and request.GET['business']:
        business = request.GET.get("business")
        results = Business.search_business(business)
        message = f'business'
        return render(request, 'search.html', {'business': results, 'message': message})
    else:
        message = "You haven't searched for anything, please try again"
    return render(request, 'search.html', {'message': message})

def signup(request):
    print('here')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)

            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration_form.html', {'form': form})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    posts = Post.objects.filter(user=current_user.id).all
    return render(request, 'registration/profile.html', {"posts": posts})

@login_required(login_url='/accounts/login/')
def update_profile(request, id):
    profile_object = get_object_or_404(Profile, user_id=id)
    user_object = get_object_or_404(User, id=id)
    update_profile = UpdateProfileForm(request.POST or None, request.FILES, instance=profile_object)
    update_user = UpdateUserForm(request.POST or None, instance=user_object)
    if update_profile.is_valid() and update_user.is_valid():
        update_profile.save()
        update_user.save()
        return HttpResponseRedirect("/profile")

    return render(request, "registration/update_profile.html", {"update_profile": update_profile, "update_user": update_user})

@login_required(login_url='/accounts/login/')
def neighbourhood(request):
    
    if request.method == 'POST':
        form = NewNeighbourhoodForm(request.POST, request.FILES)
        if form.is_valid():
            neighbourhood = form.save(commit=False)
            neighbourhood.admin = request.user

            neighbourhood.save()

        return redirect('index')

    else:
        form = NewNeighbourhoodForm()
    return render(request, 'newhood.html', {"form": form})