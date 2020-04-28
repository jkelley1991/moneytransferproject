from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ProfileUpdateForm
from django.contrib.auth.models import User
from register.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from friendship.models import Friend, FriendshipRequest
from django.views.generic import ListView
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist


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

def add_f(request,pk):
    if request.method == 'POST':
        other_user = User.objects.get(pk=pk)
        Friend.objects.add_friend(
        request.user,                               # The sender
        other_user,                                 # The recipient
        message='Hi! I would like to add you')
        # This message is optional
        return redirect('profile')

def accept(request,pk):
    if request.method == 'POST':
        friend_request = FriendshipRequest.objects.get(to_user=pk)
        friend_request.accept()
        return redirect('profile')

def users(request):
    users = User.objects.filter()

    return render(request, "main/users.html", {'users':users})

def search(request):
    if request.method == 'POST':
        srch = request.POST['srh']

        if srch:
            match = UserProfile.objects.filter(Q(email__icontains=srch))

            if match:
                return render(request,'main/search.html',{'sr':match})
            else:
                 messages.error(request,'no result found')
        else:
            return HttpResponseRedirect('/search/')
    return(render(request,'main/search.html'))
