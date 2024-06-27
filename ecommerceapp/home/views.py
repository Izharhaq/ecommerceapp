from django.shortcuts import render

def home(request):
    temlpatefilename="home/home.html"
    return render(request, temlpatefilename)


