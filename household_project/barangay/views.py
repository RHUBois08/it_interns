from django.shortcuts import render

def index_view(request):
    return render(request, 'barangay/index.html')

# Create your views here.
