from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from.models import *
from awards.models import Project

#API
from django.http import JsonResponse
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer


def registration (request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}! You are now able to login')
            return redirect ('login')
    else:
        form =UserCreationForm()
    # form=UserCreationForm()
    
    return render (request, 'users/register.html',context={'form':form})



# @login_required
# def profile(request):
#     if request.method == 'POST':
#         u_form = UserUpdateForm(request.POST, instance=request.user)
#         p_form = ProfileUpdateForm(request.POST,
#             request.FILES,
#             instance=request.user.profile)
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(request, f'Your account has been updated!')
#             return redirect('profile')

#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)

#     context = {
#         'u_form': u_form,
#         'p_form': p_form
#     }

#     return render(request, 'users/profile.html', context)


# # def user_profile(request,user_id):
# #     user_profile = Profile.objects.filter(user_id = user_id).first()
# #     images = Image.objects.filter(user_id = user_id)
# #     project = Project.objects.filter(user_id=current_user.id).all()  # get all projects

# #     return render(request, 'userprofile.html', {'user_profile':user_profile, 'images':images}) 

@login_required(login_url="/login/")
def user_profile(request):  # view profile
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()  # get profile
    project = Project.objects.filter(user_id=current_user.id).all()  # get all projects
    return render(request, "users/profile.html", {"profile": profile, "images": project}) 


@login_required(login_url="/accounts/login/")
def update_profile(request,user_id):
    if request.method == "POST":

        current_user = request.user

        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]

        bio = request.POST["bio"]
        contact = request.POST["contact"]

        profile_image = request.FILES["profile_pic"]
        profile_image = models.ImageField(default='default.jpg', upload_to='profile_pics')
        profile_url = profile_image["url"]

        user = User.objects.get(id=current_user.id)

        # check if user exists in profile table and if not create a new profile
        if Profile.objects.filter(user_id=current_user.id).exists():

            profile = Profile.objects.get(user_id=current_user.id)
            profile.image = profile_url
            profile.bio = bio
            profile.contact = contact
            profile.save()
        else:
            profile = Profile(
                user_id=current_user.id,
                profile_photo=profile_url,
                bio=bio,
                contact=contact,
            )
            profile.save_profile()

        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email

        user.save()

        return redirect("/userprofile", {"success": "Profile Updated Successfully"})

       
    else:
        return render(request, "profile.html", {"danger": "Profile Update Failed"})
    
    
    
#Rest API
class ProfileList(APIView): # get all profiles
   
    def get(self, request):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer( all_profiles , many=True)
        return Response(serializers.data)
  



