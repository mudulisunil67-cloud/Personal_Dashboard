from django.shortcuts import render,redirect, get_object_or_404
from .models import Project
from .forms import ProjectForm
from django.http import HttpResponse
from .models import Certificate
from .forms import CertificateForm

# Create your views here.
def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')


def project(request):
    project_form = ProjectForm()

    if request.method == "POST":
        project_form = ProjectForm(request.POST)

        if project_form.is_valid():
            project_form.save()
            return redirect("projects")

    all_projects = Project.objects.all().order_by("-created_at")

    return render(request, "projects.html", {
        "project_form": project_form,
        "projects": all_projects,
    })

def remove_project(request, project_id):
    if request.method == "POST":
        project = get_object_or_404(Project, id=project_id)
        project.delete()

    return redirect("projects")


def linkedin(request):
    return render(request,'linkedin.html')

def leetcode(request):
    return render(request,'leetcode.html')



def certificate(request):
    certificate_form = CertificateForm()

    if request.method == "POST":
        certificate_form = CertificateForm(request.POST)

        if certificate_form.is_valid():
            certificate_form.save()
            return redirect("certificate")

    all_certificates = Certificate.objects.all().order_by("-issue_date")

    return render(request, "certificate.html", {
        "certificate_form": certificate_form,
        "certificates": all_certificates,
    })


def help(request):
    return render(request,'help.html')






