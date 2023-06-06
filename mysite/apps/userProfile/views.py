from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PhotoForm
from django.contrib.auth import login, update_session_auth_hash
from apps.authentication.models import User


@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.cleaned_data.get('photo')
            userObject = User.objects.get(id=user.id)
            userObject.photo = photo
            userObject.save()
            update_session_auth_hash(request,user)
            return redirect('profile')
    form = PhotoForm()
    content = {
        "user": user,
        'form': form,
    }
    return render(request, 'profile.html', context=content)
