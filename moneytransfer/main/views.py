from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ProfileUpdateForm
from django.contrib.auth.models import User
from register.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from friendship.models import Friend, Follow, Block, FriendshipRequest



# Create your views here.
def home(response):
    return render(response, "main/home.html", {})

@login_required
def profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES,
        instance = request.user.userprofile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'You have successfully updated your profile information')
            return redirect('profile')
    else:
        p_form = ProfileUpdateForm(instance = request.user.userprofile)
    context = {'p_form':p_form}
    return render(request, "main/profile.html", context)

def add_contact(request):
    other_user = User.objects.get(pk=1)
    Friend.objects.add_friend(request.user,other_user)

    return render(request, 'main/profile.html')
