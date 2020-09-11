from django.shortcuts import render, redirect
from .models import Users

def index(request):
    context = {
        "all_the_users": Users.objects.all()
    }
    return render(request, "users.html", context)

def create(request):
    Users.objects.create(
        first_name = request.POST["first name"],
        last_name = request.POST["last name"],
        email_address = request.POST["email address"],
        age = request.POST["age"]
    )
    return redirect("/")

# Create your views here.
