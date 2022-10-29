from django.shortcuts import render

# Create your views here.
def play_view(request):
    return render(request, "index.html")
