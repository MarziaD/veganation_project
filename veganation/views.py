from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from veganation.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login

def index(request):
    context_dict = {}
    return render(request, 'veganation/index.html', context=context_dict)
    
def restaurants(request):
    context_dict = {}
    return render(request, 'veganation/restaurants.html', context=context_dict)
    
def protests(request):
    context_dict = {}
    return render(request, 'veganation/protests.html', context=context_dict)
    
    
def signup(request):

    registered = False
    
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
        # Did the user provide a profile picture?
        # If so, we need to get it from the input form and #put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture'] #
                profile.save()
                registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
            # Render the template depending on the context.
    return render(request, 'veganation/signup.html',
                          context = {'user_form': user_form,
                                     'profile_form': profile_form,
                                     'registered': registered})
                                     
def user_login(request):
# If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('veganation:home'))
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'veganation/index.html')
        

@login_required
def user_logout(request):
        logout(request)
        return redirect(reverse('veganation:index'))
    
