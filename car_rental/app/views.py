from django.shortcuts import render

# Create your views here.
def layouts_base(request):
    context = {
        "welcome_msg": "Welcome to Information Tracker",
    }
    return render(request, "layouts/base.html.html", context)