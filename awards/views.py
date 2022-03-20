from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *


#API
from django.http import JsonResponse
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProjectSerializer

# Create your views here.
def index(request):  
    project = Project.objects.all()
    # get the latest project from the database
    latest_project = project[0]
    # get project rating
    rating = Rating.objects.filter(project_id=latest_project.id).first()
    # print(latest_project.id)

    return render(
        request, "main/index.html", {"projects": project, "project_home": latest_project, "rating": rating}
    )

# single project page
def project_details(request, project_id):
    project = Project.objects.get(id=project_id)
    # get project rating
    rating = Rating.objects.filter(project=project)
    return render(request, "main/project.html", {"project": project, "rating": rating})

@login_required(login_url="/login/")
def save_project(request):
    if request.method == "POST":

        current_user = request.user

        title = request.POST["title"]
        location = request.POST["location"]
        description = request.POST["description"]
        url = request.POST["url"]
        image = request.FILES["image"]
        
        
        project = Project(
            user_id=current_user.id,
            title=title,
            location=location,
            description=description,
            url=url,
           
        )
        project.save_project()

        return redirect("/profile", {"success": "Project Saved Successfully"})
    else:
        return render(request, "profile.html", {"danger": "Project Save Failed"})
    
@login_required(login_url="/login/")
def delete_project(request, id):
    project = Project.objects.get(id=id)
    project.delete_project()
    return redirect("/profile", {"success": "Project Deleted Successfully"})

# rate_project
@login_required(login_url="/login/")
def rate_project(request, id):
    if request.method == "POST":

        project = Project.objects.get(id=id)
        current_user = request.user

        design_rate=request.POST["design"]
        usability_rate=request.POST["usability"]
        content_rate=request.POST["content"]

        Rating.objects.create(
            project=project,
            user=current_user,
            design_rate=design_rate,
            usability_rate=usability_rate,
            content_rate=content_rate,
            avg_rate=round((float(design_rate)+float(usability_rate)+float(content_rate))/3,2),
        )

        # get the avarage rate of the project for the three rates
        avg_rating= (int(design_rate)+int(usability_rate)+int(content_rate))/3

        # update the project with the new rate
        project.rate=avg_rating
        project.update_project()

        return render(request, "main/project.html", {"success": "Project Rated Successfully", "project": project, "rating": Rating.objects.filter(project=project)})
    else:
        project = Project.objects.get(id=id)
        return render(request, "main/project.html", {"danger": "Project Rating Failed", "project": project})


# search projects
def search_results(request):
    if 'search_term' in request.GET and request.GET["search_term"]:
        search_term = request.GET.get("search_term")
        searched_projects = Project.objects.filter(title__icontains=search_term)
        message = f"Search For: {search_term}"

        return render(request, "main/search.html", {"message": message, "projects": searched_projects})
    else:
        message = "You haven't searched for any term"
        return render(request, "main/search.html", {"message": message})  
    
# Rest Api
class ProjectList(APIView): # get all projects
   
    def get(self, request):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)