from django.shortcuts import render
import re

#importing models
from .models import UserDetail

from .forms import UserSignInForm, UserLoginForm

# Create your views here.
def layouts_base(request):
    context = {
        "welcome_msg": "Welcome to Information Tracker"
    }
    return render(request, "layouts/base.html")

def user_login(request):
    login_form = UserLoginForm()
    context = {
        "form": login_form
    }
    if request.method == "POST":
        req_email = request.POST.get("email")
        req_password = request.POST.get("password")
        try:
            std_data = UserDetail.objects.get(email=req_email)
            if std_data.password == req_password:
                return render(request, "users/dashboard.html")
            else:
                context.setdefault("msg_error", "Invalid email or password!!")
                return render(request, "users/login.html", context)
        except:
            context.setdefault("msg_error", "Invalid email or password!!")
            return render(request, "users/login.html")
    else:
        return render(request, "users/LogIn.html", context)

def user_register(request):
    reg_form = UserSignInForm()
    context = {
        "form": reg_form
    }
    if request.method == "POST":
        std_data = UserDetail()
        std_data.first_name = request.POST.get("first_name")
        std_data.middle_name = request.POST.get("middle_name")
        std_data.last_name = request.POST.get("last_name")
        std_data.contact = request.POST.get("contact")
        std_data.email = request.POST.get("email")
        std_data.password = request.POST.get("password")
        std_data.save()
    else:
        return render(request, "users/SignUp.html", context)