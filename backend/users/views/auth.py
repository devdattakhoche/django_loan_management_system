from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods
from users.decorators import authenticate_req

from users.models import User


@require_http_methods(["GET", "POST"])
def customerRegistration(request):
    if request.method == "GET":
        return render(request, "auth/registration.html")
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        u = User(name=name, email=email, password=password)
        u.set_password(password)
        u.save_customer()
        return redirect("login")


@require_http_methods(["GET", "POST"])
def userlogin(request):
    if request.method == "GET":
        return render(request, "auth/login.html")
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        print(password, email, user)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "auth/login.html", {"error": True})


@authenticate_req()
def logoutView(request, user):
    logout(request)
    return redirect("login")


@authenticate_req()
def home(request, user):
    if user.role == "Admin":
        return render(request, "admin/adminHome.html")
    if user.role == "Agent":
        return render(request, "agent/home.html")
    else:
        return redirect("customerloanlist")
