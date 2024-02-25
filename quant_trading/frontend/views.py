from django.shortcuts import render

# Create your views here.
def desktop(request):
    return render(request,'desktop.html')