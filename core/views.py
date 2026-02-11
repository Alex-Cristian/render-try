from django.shortcuts import render

def valentine(request):
    return render(request, "core/valentine.html")

def yes(request):
    return render(request, "core/yes.html")
