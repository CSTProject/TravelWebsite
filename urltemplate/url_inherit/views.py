from django.shortcuts import render

def index(request):
    content = {'text':'This is the text i am passing','number':3444}
    return render(request,"index.html",context=content)

def other(request):
    return render(request,"other.html")

