from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from neighborhoodapp.models import Business, Post, Profile, Neighbourhood
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    neighbourhoods = Neighbourhood.objects.all()
    return render(request, 'index.html', {"neighbourhoods": neighbourhoods})

def view_neighbourhood(request, id):
    neighbourhood = Neighbourhood.objects.get(id=id)
    business = Business.objects.filter(business_neighbourhood=id)
    post = Post.objects.filter(neighbourhood=id)

    # current_user = request.user
    return render(request, 'view-neighbourhood.html',  {
        'neighbourhood': neighbourhood,'business':business,'post': post
    })

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