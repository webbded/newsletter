from django.shortcuts import render

# Create your views here.

def home(request):
    title = "Welcome"
    if request.user.is_authenticated():
        title = "Hello %s " % (request.user)
    context = {
        "template_title": title
    }
    return render(request, "home.html", context)
