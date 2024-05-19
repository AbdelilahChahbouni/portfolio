from django.shortcuts import render ,get_list_or_404
from .models import Project , Tag



def home(request):
    return render(request , "home.html")


def project(request , id):
    return render(request , "project.html")

def contact(request):
    return render(request , "contact.html")





