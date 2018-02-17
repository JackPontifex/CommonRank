from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from core.models import Leaderboard, Profile
from core.forms import LeaderboardSignUpForm, ProfileSignUpForm

@login_required
def createleaderboard(request):

    if request.method == 'POST':
        newleaderboard = Leaderboard()
        newtourney.host = request.user.profile
        form = LeaderboardSignUpForm(request.POST, request.FILES, instance=newleaderboard)
        if form.is_valid():
            thisleaderboard = form.save()
            Member.objects.create(leaderboard=thisleaderboard,
                                profileuser=request.user.profile,
                                privilege=5,)
            thisleaderboard.save()
            return redirect(home)
    else:
        form = LeaderboardSignUpForm(instance=Leaderboard())
    return render(request, 'leaderboard-signup.html', {'form': form})

def profile_home(request):
    """Profile home page."""
    return render(request, 'home.html')

def profile_signup(request):
    """Profile sign up page."""
    if request.method == 'POST':
        form = ProfileSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.bio = form.cleaned_data.get('bio')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect(home)
    else:
        form = ProfileSignUpForm()
    return render(request, 'signup.html', {'form': form})
